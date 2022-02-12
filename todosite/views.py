from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm
from django.http import Http404
from django.views.generic import TemplateView
# Create your views here.


def submit(request):
    try:
        task_list = Task.objects.all().order_by('-date')
        if request.method == "POST":
            formtask = TaskForm(request.POST)
            if formtask.is_valid():
                formtask.save()
                return redirect('todosite')
        formtask = TaskForm()
        page = {
            "formtask": formtask,
            "task_list": task_list,
            "title": "TASK LIST",
        }
    except Task.DoesNotExist:
        raise Http404("Task does not exist")
    return render(request, 'pages/todowebsite.html', page)

def deleteall(request):
    item = Task.objects.all()
    page = {"item": item}
    if request.method == "POST":
        item.delete()
        return redirect('todosite')
    return render(request, 'pages/delete.html', page)

def updatetask(request, item_id):
    item = Task.objects.get(id=item_id)
    page = {"item": item}
    if request.method == "POST":
        item.title = request.POST.get('title')
        item.contents = request.POST.get('contents')
        item.save()
        return redirect ('todosite')
    return render(request, 'pages/update.html', page)

def deletetask(request, item_id):
    item = Task.objects.get(id=item_id)
    page = {"item": item}
    if request.method == "POST":
        item.delete()
        return redirect('todosite')
    return render(request, 'pages/delete.html', page)

def site(request):
    response = redirect('todosite')
    return response