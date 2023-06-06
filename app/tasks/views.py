from django.shortcuts import render, redirect
from .models import Task

# Create your views here.
def Index(request):
    return render(request, 'home.html')

def List_tasks(request):
    tasks = Task.objects.all()
    return render(request, 'list_tasks.html', {
        "tasks": tasks
    })

def Create_tasks(request):
    task = Task(title=request.POST['title'], description=request.POST['description'])
    task.save()
    return redirect('/tasks/')

def Delete_tasks(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('/tasks/')
