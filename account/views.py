from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import CustomLoginForm, CustomUserCreationForm

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('account:dashboard')
        else:
            # Add error message when authentication fails
            messages.error(request, "Something went wrong, please check the errors and try again.")
    else:
        form = CustomUserCreationForm()
    return render(request, 'authentication/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = CustomLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('account:dashboard')
        else:
            # Add error message when authentication fails
            messages.error(request, "Invalid username or password. Please check and try again.")
    else:
        form = CustomLoginForm()
    
    return render(request, 'authentication/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('account:login')

@login_required
def dashboard_view(request):
    return render(request, 'account/dashboard.html')