from django.urls import path
from accountapp.views import check_login, hello_world
from django.contrib.auth.views import LoginView

app_name = 'accountapp'
urlpatterns = [
    path('', check_login, name="checkLogin"),
    path('login/', LoginView.as_view(template_name = 'accountapp/login.html'), name='login'),
    path('hello_world/', hello_world, name='hello_world'),
]