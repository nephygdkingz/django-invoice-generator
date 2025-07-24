from django.shortcuts import render, redirect

def home(request):
    if request.user.is_authenticated:
        return redirect('account:dashboard')
    return render(request, 'frontend/home.html')