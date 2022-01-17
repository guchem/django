from django.db import models
from django.shortcuts import render, redirect
from django.views.generic import ListView, DeleteView
from .models import Todo


class TodoList(ListView):
    model = Todo
    template_name = 'todos.html'

def add_todo(request):
    if request.method=='POST':
        name = request.POST['name']
        place = request.POST['place']
        due_date = request.POST['date']
        todo = Todo.objects.create(name=name, place=place, due_date=due_date)
        return redirect('todo:list')
    return render(request, 'todos.html',)


class TodoDelete(DeleteView):
    model = Todo
    success_url = '/'