from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.

#BITCOIN IMPORT
import pybithumb as pybit

@login_required
def home(request):
    
    allInfo = pybit.get_current_price("ALL")
    context = {'allInfo' : allInfo }
    
    return render(request,'coinapp/home.html', context)

