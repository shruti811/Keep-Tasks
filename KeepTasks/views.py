from django.shortcuts import render,redirect,get_object_or_404
from .models import Task
from django.contrib import messages
from .forms import TaskForm,UpdateTaskForm
def index(request):
    tasks=Task.objects.all()
    return render(request, 'index.html', {'tasks':tasks})

def add(request):
    form = TaskForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/tasks')
    return render(request, 'add.html',{'form':form})

def details(request,id):
    task=Task.objects.get(id=id)
    return render(request, 'details.html', {'task':task})

def remove(request,id):
    task = Task.objects.get(id=id)
    task.delete()
    messages.info(request, "Task deleted successfully!")
    return redirect('/tasks')

def update(request,id):
    task=get_object_or_404(Task, id=id)
    form = UpdateTaskForm(request.POST or None, instance=task)
    if form.is_valid():
        form.save()
        return redirect('/tasks')
    return render(request, 'edit.html', {'task': form})