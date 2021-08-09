from django.contrib.auth import models, forms

class AccountUpdateForm(forms.UserCreationForm):
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].disabled = True