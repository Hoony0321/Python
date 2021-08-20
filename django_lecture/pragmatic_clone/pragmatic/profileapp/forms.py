from profileapp.models import Profile
from django.forms import ModelForm

class ProfileCreateForm(ModelForm):

    class Meta:
        model = Profile
        fields = ['image', 'nickname', 'message']
    


    