from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

app_name = 'accountapp'
# 이미 이 urls.py 분기로 들어올때 account/ 를 쓰는데 왜 또 app_name을 명시하는가?
# 나중에 accountapp만 써도 바로 갈 수 있는 함수를 설정하기 위해!
urlpatterns = [
    path('hello_world/', views.hello_world, name='hello_world'),

    path('create/', views.AccountCreateView.as_view(), name='create'),
    path('login/', LoginView.as_view(template_name = 'accountapp/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('detail/<int:pk>', views.AccountDetailView.as_view(), name='detail'),
    path('update/<int:pk>', views.AccountUpdateView.as_view(), name='update'),
]