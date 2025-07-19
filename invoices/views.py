import pandas as pd
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UploadInvoiceForm

@login_required
def upload_invoice_view(request):
    if request.method == 'POST':
        form = UploadInvoiceForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = request.FILES['file']
            try:
                if uploaded_file.name.endswith('.csv'):
                    df = pd.read_csv(uploaded_file)
                elif uploaded_file.name.endswith('.xlsx'):
                    df = pd.read_excel(uploaded_file)
                else:
                    form.add_error('file', 'Unsupported file format. Use CSV or Excel.')
                    return render(request, 'invoices/upload.html', {'form': form})
            except Exception as e:
                form.add_error('file', f'Error reading file: {str(e)}')
                return render(request, 'invoices/upload.html', {'form': form})

            # Convert DataFrame to list of dicts for template
            data = df.to_dict(orient='records')
            request.session['invoice_data'] = data  # Store in session temporarily
            return redirect('invoices:preview')
    else:
        form = UploadInvoiceForm()
    return render(request, 'invoices/upload.html', {'form': form})

@login_required
def preview_invoice_view(request):
    data = request.session.get('invoice_data', [])
    if not data:
        return redirect('upload')
    return render(request, 'invoices/preview.html', {'data': data})