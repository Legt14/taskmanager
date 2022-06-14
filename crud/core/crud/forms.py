from django import forms
from .models import TaskPost

class FormCreateTask(forms.ModelForm):
    class Meta():
        model = TaskPost
        fields = ('nameTask', 'contentTask')
