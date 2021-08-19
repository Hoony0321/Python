from django.urls import path
from accountapp.views import home
from django.contrib.auth.views import LoginView, LogoutView
from accountapp.views import AccountCreateView, AccountDetailView, AccountDeleteView, AccountUpdateView

app_name = "accountapp"
urlpatterns = [
    path('', home, name="home"),
    path('login/', LoginView.as_view(template_name="accountapp/login.html"), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('create/', AccountCreateView.as_view(), name="create"),
    path('detail/<int:pk>', AccountDetailView.as_view(), name="detail"),
    path('update/<int:pk>', AccountUpdateView.as_view(), name="update"),
    path('delete/<int:pk>', AccountDeleteView.as_view(), name="delete"),
]