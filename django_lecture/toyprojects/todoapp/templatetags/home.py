from django import template
from todoapp.models import Todo


register = template.Library()

@register.simple_tag
def get_leftItem():
    TodoList = Todo.objects.all()

    leftItem = 0
    for item in TodoList:
        if not item.complete:
            leftItem += 1
    
    return leftItem