from django import forms
from .models import tasks


class TaskForm(forms.ModelForm):
    class Meta:
        model =tasks
        fields = ['task_name', 'description','assigned_to','priority','status','due_date']
        widgets = {
            'due_date': forms.DateInput(attrs ={'type': 'date'}),
        }