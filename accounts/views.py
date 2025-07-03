from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib.auth import login

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user) 
            return redirect('task_list')
    else:
        form = RegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})