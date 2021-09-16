from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect

from .models import Note
from .forms import NoteCreateForm, NoteUpdateForm
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

class NoteDetailView(DetailView):
    model = Note;
    template_name = "noteapp/detail.html";
    context_object_name = "target_note"

class NoteDeleteView(DeleteView):
    model=Note;
    #template_name = 'noteapp/delete.html' #템플릿 없어도 됨.
    success_url = reverse_lazy('noteapp:home');

    def get(self,request,*args,**kwargs):
        return self.delete(request,*args,**kwargs); #해당 아이템 삭제


class NoteUpdateView(UpdateView):
    model = Note;
    template_name = "noteapp/update.html";
    context_object_name = "target_note"
    form_class = NoteUpdateForm;
    success_url = reverse_lazy("noteapp:home");

    



