from django.db import models
from django.utils import timezone
# Create your models here.

class TaskPost(models.Model):
    nameTask = models.CharField(max_length=250)
    contentTask = models.TextField()
    publishedTask = models.DateTimeField(default=timezone.now)
