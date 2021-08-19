from django.contrib.auth.models import User
from django.http import HttpResponseForbidden

def account_ownership_required(func):
    def decorated(request, *args, **kwargs):
        target_user = User.objects.get(pk=kwargs['pk'])
        
        if request.user == target_user: # 본인 맞음 -> 함수 제대로 작동
            return func(request, *args, **kwargs)
        else: #본인 아님 -> 잘못된 접근이라고  알려줌
            return HttpResponseForbidden()
    return decorated    
    
            

            