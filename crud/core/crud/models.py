from django.db import models
# Create your models here.

class TaskPost(models.Model):
    nameTask = models.CharField(max_length=250)
    contentTask = models.TextField()
    publishedTask = models.TimeField(auto_now=True)
