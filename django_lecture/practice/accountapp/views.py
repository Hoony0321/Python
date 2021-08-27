from django.shortcuts import render
from django.views.generic import CreateView, DetailView, DeleteView, UpdateView
from django.contrib.auth.models import User
from django.urls import reverse, reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def HomeView(request):
    user = request.user
    context = {'user':user,}

    return render(request, "accountapp/home.html", context)


class AccountCreateView(CreateView):
    model = User
    template_name = "accountapp/create.html"
    success_url = reverse_lazy("accountapp:login")
    form_class = UserCreationForm

class AccountDetailView(DetailView):
    model = User
    template_name = "accountapp/detail.html"
    context_object_name = "target_user"

class AccountUpdateView(UpdateView):
    model = User
    template_name = "accountapp/update.html"
    context_object_name = "target_user"
    form_class = "직접 만들어서 설정"

class AccountDeleteView(DeleteView):
model = User
template_name = "accountapp/delete.html"
context_object_name = "target_user"
