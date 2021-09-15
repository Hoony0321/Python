from django.urls import path

from .views import HomeView, NoteCreateView

app_name='noteapp'
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('create/', NoteCreateView.as_view(), name='create'),
]  