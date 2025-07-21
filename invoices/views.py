import pandas as pd
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from xhtml2pdf import pisa
from io import BytesIO

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

            # Add calculated columns
            df['subtotal'] = df['quantity'] * df['unit_price']
            # df['tax_amount'] = df['subtotal'] * df['tax']
            # df['total'] = df['subtotal'] + df['tax_amount']
            # grand_total = df['total'].sum()
            # sub_total = df['subtotal'].sum()
            grand_total = df['subtotal'].sum()


            # Store in session
            data = df.to_dict(orient='records')
            request.session['invoice_data'] = data
            request.session['grand_total'] = round(grand_total, 2)

            # Add invoice metadata
            request.session['invoice_info'] = {
                'invoice_number': 'INV-001',
                'date': '2025-07-21',
                'due_date': '2025-08-01',
                'company': 'Your Company',
                'company_address': '123 Business Rd.\nCity, Country 12345',
                'company_email': 'info@company.com',
                'client': 'Mark Andrew',
                'client_address': '456 Client St.\nClient City, Country'
            }

            return redirect('invoices:preview')
    else:
        form = UploadInvoiceForm()
    return render(request, 'invoices/upload.html', {'form': form})


@login_required
def preview_invoice_view(request):
    data = request.session.get('invoice_data', [])
    grand_total = request.session.get('grand_total', 0)
    invoice_info = request.session.get('invoice_info', {})
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

    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html_string.encode("utf-8")), result)

    if not pdf.err:
        response = HttpResponse(result.getvalue(), content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="invoice.pdf"'
        return response

    return HttpResponse("Error generating PDF", status=500)