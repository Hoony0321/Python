from django.shortcuts import render
from django.views.generic import CreateView, UpdateView
from profileapp.models import Profile
from profileapp.forms import ProfileCreateForm
from django.urls import reverse_lazy,reverse
# Create your views here.

class ProfileCreateView(CreateView):
    model = Profile
    form_class = ProfileCreateForm
    template_name = 'profileapp/create.html'

    def form_valid(self,form):
        temp_profile = form.save(commit=False)
        temp_profile.user = self.request.user
        temp_profile.save()

        return super().form_valid(form)

    def get_success_url(self):
        reverse('accountapp:detail', kwargs={'pk' : self.object.user.pk})

class ProfileUpdateView(UpdateView):
    model = Profile
    form_class = ProfileCreateForm
    template_name = 'profileapp/update.html'
    context_object_name ='target_profile'

    def get_success_url(self):
        reverse('accountapp:detail', kwargs={'pk' : self.object.user.pk})





