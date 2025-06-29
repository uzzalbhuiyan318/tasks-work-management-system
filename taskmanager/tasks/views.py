from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.db.models import Q
from .models import tasks  # Corrected: Use the model class name 'Task'
from .forms import TaskForm

def task_list(request):
    """
    Displays a list of all tasks with filtering, searching, sorting, and pagination.
    """
    # Start with all tasks and then apply filters
    tasks_list = tasks.objects.all()

    # Search: Filter by task name or assignee
    search_query = request.GET.get('search', '')
    if search_query:
        # Corrected: Use Q objects for OR queries and double underscore for lookups
        tasks_list = tasks_list.filter(
            Q(task_name__icontains=search_query) |
            Q(assigned_to__icontains=search_query)
        )

    # Filter by status
    status_filter = request.GET.get('status', '')
    if status_filter:
        tasks_list = tasks_list.filter(status=status_filter)

    # Filter by priority
    priority_filter = request.GET.get('priority', '')
    if priority_filter:
        tasks_list = tasks_list.filter(priority=priority_filter)

    # Filter by due date range
    start_date_filter = request.GET.get('start_date', '')
    end_date_filter = request.GET.get('end_date', '')
    if start_date_filter and end_date_filter:
        # Corrected: Use '__range' for date range filtering
        tasks_list = tasks_list.filter(due_date__range=[start_date_filter, end_date_filter])

    # Sorting
    sort_by = request.GET.get('sort', 'due_date') # Default sort by due_date
    tasks_list = tasks_list.order_by(sort_by)

    # Pagination
    paginator = Paginator(tasks_list, 10)  # Show 10 tasks per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # Corrected: This return statement should be at the end of the function
    return render(request, 'tasks/task_list.html', {'page_obj': page_obj})


def task_detail(request, pk):
    """
    Displays the details of a single task.
    """
    # Corrected: Pass the primary key (pk) to get the specific task
    task = get_object_or_404(tasks, pk=pk)
    # Corrected: Template name and context variable were wrong
    return render(request, 'tasks/task_detail.html', {'task': task})


def task_create(request):
    """
    Creates a new task.
    """
    if request.method == "POST":
        form = TaskForm(request.POST)
        # Corrected: Method is 'is_valid()', not 'Is_Valid()'
        if form.is_valid():
            form.save()
            # Corrected: URL name should be a string
            return redirect("task_list")
    else:
        # Corrected: Create an instance of the form
        form = TaskForm()
    
    # This return handles both the initial GET request and the case where the POST form is invalid
    return render(request, 'tasks/task_form.html', {'form': form})


def task_update(request, pk):
    """
    Updates an existing task.
    """
    # Corrected: Pass pk to get the specific task to update
    task = get_object_or_404(tasks, pk=pk)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'tasks/task_form.html', {'form': form})


def task_delete(request, pk):
    """
    Deletes a task after confirmation.
    """
    # Corrected: Pass pk to get the specific task to delete
    task = get_object_or_404(tasks, pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request, 'tasks/task_confirm_delete.html', {'task': task})
