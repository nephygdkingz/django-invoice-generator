import pandas as pd
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from weasyprint import HTML
from django.http import HttpResponse

from .forms import UploadInvoiceForm, InvoiceForm
from .utils import generate_invoice_number


@login_required
def upload_invoice_view(request):
    if request.method == 'POST':
        form = UploadInvoiceForm(request.POST, request.FILES)
        invoice_form = InvoiceForm(request.POST, request.FILES)

        if form.is_valid() and invoice_form.is_valid():
            uploaded_file = request.FILES['file']
            try:
                if uploaded_file.name.endswith('.csv'):
                    df = pd.read_csv(uploaded_file)
                elif uploaded_file.name.endswith('.xlsx'):
                    df = pd.read_excel(uploaded_file)
                else:
                    form.add_error('file', 'Unsupported file format. Use CSV or Excel.')
                    return render(request, 'invoices/upload.html', {'form': form, 'invoice_form': invoice_form})
            except Exception as e:
                form.add_error('file', f'Error reading file: {str(e)}')
                return render(request, 'invoices/upload.html', {'form': form, 'invoice_form': invoice_form})

            # Add calculated columns
            df['subtotal'] = df['quantity'] * df['unit_price']
            grand_total = df['subtotal'].sum()


            # Store in session
            data = df.to_dict(orient='records')
            request.session['invoice_data'] = data
            request.session['grand_total'] = round(grand_total, 2)
            request.session['invoice_info'] = invoice_form.cleaned_data
            request.session['invoice_number'] = generate_invoice_number()
            return redirect('invoices:preview')
    else:
        form = UploadInvoiceForm()
        invoice_form = InvoiceForm()
    return render(request, 'invoices/upload.html', {'form': form, 'invoice_form': invoice_form})


@login_required
def preview_invoice_view(request):
    data = request.session.get('invoice_data', [])
    grand_total = request.session.get('grand_total', 0)
    invoice_info = request.session.get('invoice_info', {})
    invoice_number = request.session.get('invoice_number', generate_invoice_number())
    if not data:
        return redirect('invoices:upload')
    return render(request, 'invoices/preview.html', {
        'data': data,
        'grand_total': round(grand_total, 2),
        'invoice_info': invoice_info
    })


@login_required
def download_invoice_pdf_view(request):
    data = request.session.get('invoice_data', [])
    grand_total = request.session.get('grand_total', 0)
    invoice_info = request.session.get('invoice_info', {})

    # calculate tax rate
    tax_rate = 10  # percent
    tax_amount = round((tax_rate / 100) * grand_total, 2)
    total_due = round(grand_total + tax_amount, 2)
    if not data:
        return redirect('invoices:upload')

    html_string = render_to_string('invoices/invoice_template_pdf.html', {
        'data': data,
        'total_due': total_due,
        'grand_total': round(grand_total, 2),
        'invoice_info': invoice_info,
        'tax_rate': 10,  # assuming 10%
        'tax_amount': tax_amount,
    })
    html = HTML(string=html_string)
    pdf = html.write_pdf()

    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="invoice.pdf"'
    return response
    