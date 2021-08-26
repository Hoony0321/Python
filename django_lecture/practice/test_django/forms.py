from django import forms
from test_django.models import UserRevised, Book

class NameForm(forms.Form):
    your_name = forms.EmailField(label="Your Name" ,max_length=100)

class UserCreateForm(forms.ModelForm):
    
    class Meta:
        model = UserRevised
        fields = ['username', 'password', 'nickname']

class BookCreateForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = ['title', 'author', 'price', 'published_date']
        
