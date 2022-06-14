from django.shortcuts import redirect, render
from django.views import View
from .forms import FormCreateTask
from .models import TaskPost
# Create your views here.

class Task(View):
    def get(self, request, *args, **kwargs):
        posts = TaskPost.objects.all()
        context ={
            "posts":posts
        }
        return render(request, 'task.html', context)

class CreateTask(View):
    def get(self, request, *args, **kwargs):
        form = FormCreateTask()
        context={
            "form":form
        }
        return render(request, 'createTask.html', context)

    def post(self, request, *args, **kwargs):
        if request.method=="POST":
            form = FormCreateTask(request.POST)
            if form.is_valid():
                nameTask = form.cleaned_data.get("nameTask")
                contentTask = form.cleaned_data.get("contentTask")
                p, created = TaskPost.objects.get_or_create(nameTask=nameTask, contentTask=contentTask)
                p.save()
                return redirect('crud:task')
        context = {}
        
        return render(request, "createTask.html", context)
