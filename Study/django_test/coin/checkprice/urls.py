from django.urls import path

from . import views

app_name = 'check'
urlpatterns = [
    path('', views.index, name='index'),
    path('ajax/' , views.ajax_home, name="ajax"),
    path('ajax/reponse/' , views.ajax_reponse, name='reponse'),
]