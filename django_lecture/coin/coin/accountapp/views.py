from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth import models, forms
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
# Create your views here.

def hello_world(request):
    return render(request, 'accountapp/hello_world.html');

def check_login(request):

    if request.user.is_anonymous:
        # 로그인  안 되어있는 상태
        return HttpResponseRedirect(reverse('accountapp:login')); 
    else:  
        # 로그인 되어있는 상태
        pass

class AccountCreateView(CreateView):
    model = models.User
    form_class = forms.UserCreationForm
    success_url = reverse_lazy("accountapp:home")
    template_name = 'accountapp/create.html'

class AccountDetailView(DetailView):
    

