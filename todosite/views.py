from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm
from django.http import Http404
# Create your views here.


def submit(request):
    try:
        task_list = Task.objects.all()
        if request.method == "POST":
            form = TaskForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('todosite')
        form = TaskForm()
        page = {
            "forms": form,
            "task_list": task_list,
            "title": "TASK LIST",
        }
    except Task.DoesNotExist:
        raise Http404("Task does not exist")
    return render(request, 'pages/todowebsite.html', page)
