from django.urls import path
from .views import Task, CreateTask

app_name = 'crud'

urlpatterns = [
    path("", Task.as_view(), name= 'task'),
    path('createtask/', CreateTask.as_view(), name='create'),
]
