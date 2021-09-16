from django import forms
from .views import Note

class NoteCreateForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'content']


class NoteUpdateForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'content']
