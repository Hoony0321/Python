from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def hello_world(request): #인자로 request가 들어가는 이유는 client에게 요청을 받아 처리하기 때문!
    
    if request.method == "POST":
        return render(request, 'accountapp/hello_world.html' , context ={ 'text' : "POST METHOD"});
    else :
        return render(request, 'accountapp/hello_world.html');