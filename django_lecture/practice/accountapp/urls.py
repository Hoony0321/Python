from django.urls import path
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView

from accountapp.views import HomeView, AccountCreateView, AccountDetailView


app_name = 'accountapp'
urlpatterns = [
    path('home/', HomeView, name='home'),
    path('login/', LoginView.as_view(template_name='accountapp/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('create/', AccountCreateView.as_view(), name='create'),
    path('detail/<int:pk>', AccountDetailView.as_view(), name='detail'),
    
]