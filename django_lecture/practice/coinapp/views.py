from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from profileapp.models import Profile
from coinapp.decorators import account_has_profile



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
@account_has_profile
def home(request):
    
    allInfo = pybit.get_current_price("ALL")

    number_of_object_in_page = 20
    paginator = Paginator(tuple(allInfo.items()), number_of_object_in_page)
    page = request.GET.get('page' , 1)
    post = paginator.get_page(page)

    favorite = request.user.profile.favorite
    
    return render(request,'coinapp/home.html', {'post' : post , 'favorite' : favorite } )


@account_has_profile
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

    ###FAVORITE 설정
    favorite = False

    json_data = request.user.profile.favorite

    if not json_data is None:
        #None이 아닐 경우
        favorite_list = json.loads(json_data)
        if currency in favorite_list:
            favorite = True
    

    
    
    

    return render(request, 'coinapp/detail.html', {'currency' : currency , 'plot1_script' : script, 'plot1_div' : div , 'period' : period , 'favorite' : favorite })

@account_has_profile
def FavoriteView(request):
    curUser = request.user
    data = None

    if request.method == 'POST':

        addItem = request.POST.get('add', None)
        deleteItem = request.POST.get('delete', None)

        if not addItem == None:
            #새로운 favorite item 추가
            if curUser.profile.favorite == None:
                #favorite가 null일 경우 -> 새롭게 배열 생성
                favorite_list = [addItem]
                Profile.objects.filter(user=curUser).update(favorite=json.dumps(favorite_list))
            else:
                #favorite가 존재할 경우 -> 배열 뒤에 addItem 추가
                favorite_list = json.loads(curUser.profile.favorite)
                favorite_list.append(addItem)
                Profile.objects.filter(user=curUser).update(favorite=json.dumps(favorite_list))
        else:
            #기존 favorite item 삭제
            favorite_list = json.loads(curUser.profile.favorite)
            favorite_list.remove(deleteItem)
            Profile.objects.filter(user=curUser).update(favorite=json.dumps(favorite_list))


    
    else: #request.method = GET

        json_data = curUser.profile.favorite

        if not json_data is None:
            #Profile favorite 가져오기
            favorite_list = json.loads(curUser.profile.favorite)
            allInfo = pybit.get_current_price("ALL")
            info = {}
            for ticker in favorite_list:
                ticker_info = allInfo[ticker]
                info[ticker] = ticker_info
        
            #pagination 하기
            number_of_object_in_page = 10
            paginator = Paginator(tuple(info.items()), number_of_object_in_page)
            page = request.GET.get('page' , 1)
            post = paginator.get_page(page)

            data = post
            
            if paginator.count == 0: data = None
        
    return render(request, 'coinapp/favorite.html', { 'data' : data } )
    
