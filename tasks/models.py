from django.db import models
from django.utils import timezone

# Create your models here.

class tasks(models.Model):
    Priority_Choice = [
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High')
    ]
    
    Status_Choice = [
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed')
    ]
    
    task_name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    assigned_to = models.CharField(max_length=255)
    priority = models.CharField(max_length=20, choices=Priority_Choice, default='Medium')
    status = models.CharField(max_length=20, choices=Status_Choice, default='Pending')
    due_date = models.DateField()
    created_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.task_name
    
    