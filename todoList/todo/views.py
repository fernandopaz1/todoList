# from todoList import todo
from django.shortcuts import render, get_object_or_404
from .models import Todo
from django.utils import timezone

# Create your views here.
def todo_list(request):
    todos = Todo.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'todo/todo_list.html', {'todos': todos})

def todo_details(request, pk):
    todos = get_object_or_404(Todo, pk=pk)
    return render(request, 'todo/todo_detail.html', {'todo': todos})

def todo_delete(request, pk):
    Todo.delete_todo(pk)
    todos = Todo.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'todo/todo_list.html', {'todos': todos}) 

def change_state(request, pk, state):
    Todo.change_state(pk, state)
    todos = Todo.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'todo/todo_list.html', {'todos': todos}) 