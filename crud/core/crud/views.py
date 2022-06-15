from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic.edit import View, DeleteView
from .forms import FormCreateTask
from .models import TaskPost
from django.urls import reverse_lazy
# Create your views here.

class BaseView(View):
    def get(self, request, *args, **kwargs):

        return render(request, 'base.html')

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

class DetailTask(View):
    def get(self, request, pk, *args, **kwargs):
        post = get_object_or_404(TaskPost, pk=pk)
        context = {
            'post':post
        }
        return render(request, 'detailTask.html', context)



class DeleteTask(DeleteView):
    model = TaskPost
    template_name = 'deleteTask.html'
    success_url = reverse_lazy('crud:task')
