from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect

from .models import Todo

import json
# Create your views here.

class HomeView(ListView):
    model = Todo
    template_name = 'todoapp/home.html'
    context_object_name = 'todoList'


    def post(self,request,*args,**kwargs):


        if 'todo_field' in request.POST: #CASE 1 : 사용자가 데이터를 입력했을 경우  
            todoName = request.POST.get('todo_field')

            #new_todo_item 설정 * 값 세팅 (complete값은 default로)
            new_todo_item = Todo()
            new_todo_item.name = todoName 
            new_todo_item.save()

        elif 'complete' in request.POST: #CASE 2 : 사용자가 complete_btn을 클릭했을 경우
            recieve_data = json.loads(request.POST.get("complete"));
            
            todoObj = Todo.objects.filter(name=recieve_data[0]);
            todoObj.update(complete= True if recieve_data[1] else False );

        elif 'delete' in request.POST: #CASE 3 : 사용자가 clear_btn을 클릭했을 경우
            completeList = json.loads(request.POST.get("delete"));
            
            for _name in completeList:
                Todo.objects.filter(name=_name).delete();


        #get방식 page로 리턴
        return HttpResponseRedirect(reverse_lazy('todoapp:home'))

    


