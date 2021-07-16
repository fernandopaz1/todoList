from django.shortcuts import render
from .models import Todo
from django.utils import timezone

# Create your views here.
def todo_list(request):
    todos = Todo.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'todo/todo_list.html', {'todos': todos})

