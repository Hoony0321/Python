from django.shortcuts import render
from django.views.generic import UpdateView, CreateView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator

from .models import Profile
from .forms import ProfileCreateForm
from .decorators import profile_ownership_required


# Create your views here.

class ProfileCreateView(CreateView):
    model = Profile
    template_name = "profileapp/create.html"
    form_class = ProfileCreateForm
    context_object_name = "target_profile"

    def form_valid(self, form):
        temp_profile = form.save(commit=False)
        temp_profile.user = self.request.user
        temp_profile.save()

        return super().form_valid(form)


    def get_success_url(self):
        return reverse_lazy("accountapp:detail", kwargs={'pk' : self.object.user.pk })

@method_decorator(profile_ownership_required, 'get')
@method_decorator(profile_ownership_required, 'post')
class ProfileUpdateView(UpdateView):
    model = Profile
    template_name = "profileapp/update.html"
    context_object_name = "target_profile"
    form_class = ProfileCreateForm

    def get_success_url(self):
        return reverse_lazy("accountapp:detail", kwargs={'pk' : self.object.user.pk })
