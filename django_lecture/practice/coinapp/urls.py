from django.urls import path


from .views import home

app_name="coinapp"
urlpatterns = [
    path("home/", home, name="home"),
]