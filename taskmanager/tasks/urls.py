from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),
    
    # This URL is for the "Add New Task" modal
    path('task/new/', views.task_create, name='task_create'),
    
    # These URLs are for the View, Update, and Delete modals
    path('task/<int:pk>/', views.task_detail, name='task_detail'),
    path('task/<int:pk>/update/', views.task_update, name='task_update'), # This path is crucial for the Edit button
    path('task/<int:pk>/delete/', views.task_delete, name='task_delete'),
]