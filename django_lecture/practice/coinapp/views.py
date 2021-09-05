from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from profileapp.models import Profile
# Create your views here.

#BITCOIN IMPORT
import pybithumb as pybit
from pandas import DataFrame, Series

#CHART MAKER
from bokeh.plotting import figure
from bokeh.embed import json_item
from bokeh.embed import components
from bokeh.models.formatters import NumeralTickFormatter
import json
import pandas as pd



@login_required
def home(request):
    
    allInfo = pybit.get_current_price("ALL")

    number_of_object_in_page = 20
    paginator = Paginator(tuple(allInfo.items()), number_of_object_in_page)
    page = request.GET.get('page' , 1)
    post = paginator.get_page(page)
    
    return render(request,'coinapp/home.html', {'post' : post } )

def DetailView(request):
    
    currency = request.GET.get('currency', 'BTC')
    period = request.GET.get('period', 'M')

    temp_data = pybit.get_ohlcv(currency)

    how = {
        'open' : 'first',
        'close' : 'last',
        'high' : 'max',
        'low' : 'min',
        'volume' : 'sum',
    }

    data_resample = temp_data.resample(period).apply(how)

    data = data_resample.reset_index()
    

    inc = data.close >= data.open
    dec = data.open > data.close

    

    p_candlechart = figure(plot_width=1000, plot_height=200, x_range=(-1, len(data)), tools="crosshair", sizing_mode='stretch_both')
    p_candlechart.segment(data.index[inc], data.high[inc], data.index[inc], data.low[inc], color="red")
    p_candlechart.segment(data.index[dec], data.high[dec], data.index[dec], data.low[dec], color="blue")
    p_candlechart.vbar(x=data.index[inc], width=0.5, top=data.open[inc], bottom=data.close[inc], fill_color="red", line_color="red")
    p_candlechart.vbar(x=data.index[dec], width=0.5, top=data.open[dec], bottom=data.close[dec], fill_color="blue", line_color="blue")

   

    p_volumechart = figure(plot_width=1000, plot_height=100, x_range=p_candlechart.x_range, tools="crosshair", sizing_mode='stretch_both')
    p_volumechart.vbar(data.index, 0.5, data.volume, fill_color="black", line_color="black")

    p_candlechart.yaxis[0].formatter = NumeralTickFormatter(format='0,0')
    p_candlechart.xaxis.visible = False    

    major_label = {
        i: date.strftime('%Y%m%d') for i, date in enumerate(pd.to_datetime(data['time']))
    }
    major_label.update({len(data): ''})
    p_volumechart.xaxis.major_label_overrides = major_label
    p_volumechart.yaxis[0].formatter = NumeralTickFormatter(format='0,0')

    ####CHART DRAW####
    from bokeh.layouts import gridplot

    plot = gridplot([[p_candlechart], [p_volumechart]], toolbar_location=None)

    script, div = components(plot)

    return render(request, 'coinapp/detail.html', {'currency' : currency , 'plot1_script' : script, 'plot1_div' : div , 'period' : period })


def FavoriteView(request):
    curUser = request.user

    if request.method == 'POST':

        currency = request.POST['data']
        if curUser.profile.favorite == None:
            temp_dict = {'1' : currency}
            Profile.objects.filter(user=request.user).update(favorite=json.dumps(temp_dict))
        else:
            temp_dict = json.loads(curUser.profile.favorite)
            index = '2'
            while(True):
                if not index in temp_dict:
                    temp_dict[2] = currency
                    break
                
                index = str(int(index) + 1)

            
            print(temp_dict)
    
    else:
        Profile.objects.filter(user=request.user).update(favorite=None)
        
    return render(request, 'coinapp/favorite.html', { 'data' : "NONE" } )
    
