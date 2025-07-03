from django.contrib import admin
from .models import tasks

# Register your models here.
@admin.register(tasks)
class TasksAdmin(admin.ModelAdmin):
    list_display =('task_name', 'description', 'assigned_to', 'priority', 'status','due_date', 'created_date')
    list_filter =('status', 'priority', 'due_date')
    search_fields = ('task_name', 'assigned_to')

    # This is the new line that adds pagination
    list_per_page = 10