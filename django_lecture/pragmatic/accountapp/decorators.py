from django.contrib.auth import models
from django.http import HttpResponseForbidden


def account_ownership_required(func):
    def decorated(request, *args, **kwargs):
        user = models.User.objects.get(pk=kwargs['pk'])
        if not user == request.user:
            return HttpResponseForbidden()
        else:
            return func(request,*args,**kwargs)
    return decorated


