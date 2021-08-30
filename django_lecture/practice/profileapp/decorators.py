from profileapp.models import Profile
from django.http import HttpResponseForbidden

def profile_ownership_required(func):
    def decorator(request, *args, **kwagrs):
        target_profile = Profile.objects.get(pk=kwagrs['pk'])

        if request.user == target_profile.user:
            return func(request, *args, **kwagrs)
        else:
            return HttpResponseForbidden()
    return decorator

    
