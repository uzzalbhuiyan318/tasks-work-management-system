from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    # Use Django's built-in LoginView. It will look for 'registration/login.html'
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    # Use Django's built-in LogoutView.
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
