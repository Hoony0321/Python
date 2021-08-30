from django.contrib.auth.models import User
from django.http import HttpResponseForbidden

def account_ownership_required(func):
    def decorator(request,*args, **kwargs):
        target_user = User.objects.get(pk=kwargs['pk'])

        if request.user == target_user:
            return func(request, *args, **kwargs)
        else:
            return HttpResponseForbidden()
    return decorator
        
