from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

# Create your views here.

#login 되어있을 시 login_redirect_url로 이동
#login 안 되어있을 시 logout_redirect_url로 이동
@login_required 
def home(request):
    return render(request, template_name="home.html")
        


class AccountCreateView(CreateView):
    model = User
    template_name = 'accountapp/create.html'
    success_url = reverse_lazy('accountapp:home')
    form_class = UserCreationForm



    
