from django.urls import path
from .views import BaseView, Task, CreateTask, DetailTask, DeleteTask
#import request
app_name = 'crud'

urlpatterns = [
    path("", BaseView.as_view(), name='base'),
    path("task", Task.as_view(), name= 'task'),
    path('createtask/', CreateTask.as_view(), name='create'),
    path('<int:pk>/detail', DetailTask.as_view(), name='detail'),
    path('<int:pk>/delete/', DeleteTask.as_view(), name='delete')
]
