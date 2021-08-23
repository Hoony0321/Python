from django.shortcuts import render
from test_django.forms import NameForm
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.

def get_name(request):

    if request.method == 'POST':

        form = NameForm(request.POST)

        if form.is_valid():
            
            return HttpResponseRedirect(reverse('testapp:resultForm'))

    
    else: #GET METHOD
        form = NameForm()
    
    return render(request, 'test_django/name.html', {'form':form})