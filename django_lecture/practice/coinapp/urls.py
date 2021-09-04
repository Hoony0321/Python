from django.urls import path


from .views import home, DetailView

app_name="coinapp"
urlpatterns = [
    path("home/", home, name="home"),
    path("detail/", DetailView, name="detail")
]