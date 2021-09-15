from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy

from .models import Note
from .forms import NoteCreateForm
# Create your views here.

class HomeView(ListView):
    model = Note;
    template_name = "noteapp/home.html";
    context_object_name = "noteList"

class NoteCreateView(CreateView):
    model = Note;
    template_name = "noteapp/create.html";
    form_class = NoteCreateForm;
    success_url = reverse_lazy("noteapp:home");
    



