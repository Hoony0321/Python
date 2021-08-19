from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from accountapp.forms import AccountUpdateForm
from accountapp.decorators import account_ownership_required
from django.utils.decorators import method_decorator

# decorator settings
has_ownership = [account_ownership_required, login_required]

# Create your views here.

#login 되어있을 시 login_redirect_url로 이동
#login 안 되어있을 시 logout_redirect_url로 이동
@login_required 
def home(request):
    target_user = request.user
    context = {'target_user' : target_user}
    return render(request, "home.html", context)
        

class AccountCreateView(CreateView):
    model = User
    template_name = 'accountapp/create.html'
    success_url = reverse_lazy('accountapp:home')
    form_class = UserCreationForm


class AccountDetailView(DetailView):
    model = User
    template_name = 'accountapp/detail.html'
    context_object_name = 'target_user'

@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountUpdateView(UpdateView):
    model = User
    template_name = 'accountapp/update.html'
    context_object_name = 'target_user'
    form_class = AccountUpdateForm
    success_url = reverse_lazy('accountapp:home')

@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountDeleteView(DeleteView):
    model = User
    template_name = 'accountapp/delete.html'
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:login')






    
