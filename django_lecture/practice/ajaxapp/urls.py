from django.urls import path

from .views import HomeView, SendView

app_name='ajaxapp'
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('send/', SendView.as_view(), name='send')
]