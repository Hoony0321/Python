from django.shortcuts import render
from django.views.generic import TemplateView, FormView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect

from .forms import SendForm
from .models import HelloWorld
# Create your views here.

class HomeView(TemplateView):
    template_name = 'ajaxapp/home.html'

    def post(self,request,*args, **kwargs):
        context = self.get_context_data(**kwargs)
        new_hello_world = HelloWorld()
        new_hello_world.text = context['data']
        new_hello_world.save()

        # return self.render_to_response(context) -> 새로고침 할 경우 계속 오브젝트가 저장됨.

        return HttpResponseRedirect(reverse_lazy('ajaxapp:home'))

    def get(self,request,*args,**kwargs):
        hello_world_list = HelloWorld.objects.all()
        context = self.get_context_data(**kwargs)
        context['hello_world_list'] = hello_world_list
        return self.render_to_response(context)

    def get_context_data(self, *args, **kwargs):
        #POST METHOD
        if self.request.method == "POST":
            data = self.request.POST.get("data")
            
            #data is None
            if data is None:
                data = 'NONE DATA'
            #data has value
            else: 
                print(data)
                data = 'PASSING DATA : ' + data

            context = super(HomeView, self).get_context_data(*args, **kwargs)
            context['data'] = data
            return context
        
        # GET METHOD
        else: 
            context = super(HomeView, self).get_context_data(*args, **kwargs)
            return context


class SendView(FormView):
    template_name = 'ajaxapp/send.html'
    form_class = SendForm
    success_url = reverse_lazy('ajaxapp:home')


