from django import forms
from test_django.models import UserRevised

class NameForm(forms.Form):
    your_name = forms.EmailField(label="Your Name" ,max_length=100)

class UserCreateForm(forms.ModelForm):
    
    class Meta:
        model = UserRevised
        fields = ['username', 'password', 'nickname']

