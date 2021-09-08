from django.contrib.auth.models import User
from django.http import HttpResponseForbidden
from django.urls import reverse_lazy
from django.shortcuts import render, HttpResponseRedirect

def account_has_profile(func):
    def decorator(request,*args, **kwargs):
        try:
            if request.user.profile:
            #PROFILE 존재 O
                return func(request, *args, **kwargs)
        except Exception as ex:
            #PROFILE 존재 X
            print("에러 내용 : ",ex)
            return HttpResponseRedirect(reverse_lazy('accountapp:detail',kwargs={'pk' : request.user.pk}))
    return decorator
        
