from django import forms

class SendForm(forms.Form):
    name = forms.CharField(max_length=10)
    data = forms.CharField(max_length=100)