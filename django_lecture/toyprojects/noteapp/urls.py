from django.urls import path

from .views import HomeView, NoteCreateView, NoteDetailView, NoteUpdateView, NoteDeleteView

app_name='noteapp'
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('create/', NoteCreateView.as_view(), name='create'),
    path('detail/<int:pk>', NoteDetailView.as_view(), name='detail'),
    path('update/<int:pk>', NoteUpdateView.as_view(), name="update"),
    path('delete/<int:pk>', NoteDeleteView.as_view(), name="delete"),
]  