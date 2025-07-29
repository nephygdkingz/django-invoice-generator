from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import FileResponse, Http404
from django.shortcuts import get_object_or_404

from .forms import CustomLoginForm, CustomUserCreationForm
from invoices.models import InvoiceHistory

def register_view(request):
    if request.user.is_authenticated:
        return redirect('account:dashboard')
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
    if request.user.is_authenticated:
        return redirect('account:dashboard')
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
    invoices = InvoiceHistory.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'account/dashboard.html', {'invoices': invoices})


@login_required
def download_saved_invoice_view(request, invoice_id):
    invoice = get_object_or_404(InvoiceHistory, id=invoice_id, user=request.user)

    if not invoice.pdf_file:
        raise Http404("PDF file not found.")

    try:
        return FileResponse(invoice.pdf_file.open('rb'), as_attachment=True, filename=invoice.pdf_file.name)
    except FileNotFoundError:
        raise Http404("PDF file is missing on the server.")