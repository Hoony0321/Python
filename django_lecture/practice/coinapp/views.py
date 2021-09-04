from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
# Create your views here.

#BITCOIN IMPORT
import pybithumb as pybit

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

    info = pybit.get_current_price("BTC")

    return render(request, 'coinapp/detail.html', {'currency' : currency})

