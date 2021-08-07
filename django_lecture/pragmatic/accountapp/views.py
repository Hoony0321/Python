from django.shortcuts import render
from django.http import HttpResponse
from accountapp.models import HelloWorld
# Create your views here.

def hello_world(request): #인자로 request가 들어가는 이유는 client에게 요청을 받아 처리하기 때문!
    
    if request.method == "POST":

        temp = request.POST.get('hello_world_input');
        
        new_hello_world = HelloWorld();
        new_hello_world.text = temp;
        new_hello_world.save();

        return render(request, 'accountapp/hello_world.html' , context ={ 'hello_world_output' : new_hello_world });
    
    else :
        return render(request, 'accountapp/hello_world.html');