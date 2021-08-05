from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import generic

from .models import Currency

import datetime
import pybithumb as pybit
import json
# Create your views here.

def getCurrency(ticker, info):
    
    currencyItem = Currency();
    for k, data in info.items():
        if(k == ticker):
            currencyItem.name = ticker;
            currencyItem.price = data['closing_price'];
            currencyItem.change_rate = data['fluctate_rate_24H'];
            currencyItem.volume = data['units_traded'];
            break;
    
    return currencyItem;

def currencyList_update():
    currency_list = Currency.objects.all();
    info = pybit.get_current_price("ALL");

    for item in currency_list:
        currencyItem = getCurrency(item.name, info);
        item.price = currencyItem.price;
        item.change_rate = currencyItem.change_rate;
        item.volume = currencyItem.volume;
        item.save()

        


def index(request):
    
    now = datetime.datetime.now();
    time_utf = now.strftime("%Y-%m-%d      %H:%M:%S");
    time_korea = (now + datetime.timedelta(hours=9)).strftime("%Y-%m-%d      %H:%M:%S");

    currencyList_update();
    currency_list = Currency.objects.all();
    
    context = {
        'currency_list' : currency_list,
        'time_utf' : time_utf,
        'time_korea' : time_korea,
        };
    return render(request, 'check/index.html', context);


def ajax_home(request):
    return render(request, 'check/ajax.html');
 
def ajax_reponse(request):
    jsonObject = json.loads((request.body).decode('utf-8'));
    return JsonResponse(jsonObject);

