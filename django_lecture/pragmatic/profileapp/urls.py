from django.urls import path
from . import views

app_name = 'profileapp'
# 이미 이 urls.py 분기로 들어올때 account/ 를 쓰는데 왜 또 app_name을 명시하는가?
# 나중에 accountapp만 써도 바로 갈 수 있는 함수를 설정하기 위해!
urlpatterns = [
    
]