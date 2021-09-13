from django.shortcuts import render
from django.views.generic import ListView

from .models import Note
# Create your views here.

class HomeView(ListView):
    model = Note;
    template_name = "noteapp/home.html";
    



