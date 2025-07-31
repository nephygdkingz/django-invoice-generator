import pandas as pd
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from weasyprint import HTML
from django.http import HttpResponse
from datetime import date
from django.conf import settings
from django.core.files.base import ContentFile
from django.contrib import messages

from .forms import UploadInvoiceForm, InvoiceForm
from .utils import generate_invoice_number, save_temp_uploaded_file, load_temp_uploaded_file
from .models import InvoiceHistory


@login_required
def upload_invoice_view(request):
    if request.method == 'POST':
        form = UploadInvoiceForm(request.POST, request.FILES)
        invoice_form = InvoiceForm(request.POST, request.FILES)

        if form.is_valid() and invoice_form.is_valid():
            # uploaded_file = request.FILES['file']
            uploaded_file = request.FILES.get('file')

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

            # Clean invoice info (excluding file-like objects)
            invoice_info = {
                k: (
                    # convert date to string
                    v.isoformat() if isinstance(v, date) else v  
                )
                for k, v in invoice_form.cleaned_data.items()
                if not hasattr(v, 'read')  # skip files like company_logo
            }

            # ✅ Save logo separately and store path in session
            # logo_file = request.FILES['company_logo']
            logo_file = request.FILES.get('company_logo')
            if logo_file:
                logo_path = save_temp_uploaded_file(logo_file)
                request.session['company_logo_path'] = logo_path

            # ✅ Store data in session
            request.session['invoice_data'] = df.to_dict(orient='records')
            request.session['grand_total'] = round(grand_total, 2)
            request.session['invoice_info'] = invoice_info
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

    # Calculate totals
    tax_rate = 10  # percent
    tax_amount = round((tax_rate / 100) * grand_total, 2)
    total_due = round(grand_total + tax_amount, 2)

    # Check if user is paid
    is_paid = request.user.userprofile.is_paid

    # Get logo URL from stored path
    logo_path = request.session.get('company_logo_path')
    logo_url = None

    # Only use session-stored logo path if the user is paid
    if is_paid and logo_path:
        logo_url = settings.MEDIA_URL + logo_path 

    return render(request, 'invoices/invoice_preview_main.html', {
        'data': data,
        'total_due': total_due,
        'grand_total': round(grand_total, 2),
        'invoice_info': invoice_info,
        'tax_rate': tax_rate,
        'tax_amount': tax_amount,
        'invoice_number': invoice_number,
        'logo_url': logo_url,
    })

@login_required
def download_invoice_pdf_view(request):
    data = request.session.get('invoice_data', [])
    grand_total = request.session.get('grand_total', 0)
    invoice_info = request.session.get('invoice_info', {})
    invoice_number = request.session.get('invoice_number', generate_invoice_number())

    if not data or not invoice_info:
        return redirect('invoices:upload')

    tax_rate = 10  # percent
    tax_amount = round((tax_rate / 100) * grand_total, 2)
    total_due = round(grand_total + tax_amount, 2)

    is_paid = request.user.userprofile.is_paid

    # check if user is subscribed
    if not is_paid:
        invoice_count = InvoiceHistory.objects.filter(user=request.user).count()
        if invoice_count >= 4:
            messages.error(request, "Free users are limited to 4 invoices. Upgrade to Pro to generate more.")
            return redirect('invoices:upgrade')

    # Get logo URL from stored path
    logo_path = request.session.get('company_logo_path')
    logo_url = None

    if is_paid and logo_path:
        logo_url = request.build_absolute_uri(settings.MEDIA_URL + logo_path)

    html_string = render_to_string('invoices/invoice_template_pdf.html', {
        'data': data,
        'total_due': total_due,
        'grand_total': round(grand_total, 2),
        'invoice_info': invoice_info,
        'tax_rate': tax_rate,
        'tax_amount': tax_amount,
        'invoice_number': invoice_number,
        'logo_url': logo_url,
    })

    html = HTML(string=html_string)
    pdf = html.write_pdf()

    pdf_filename = f"{invoice_number}.pdf"
    invoice = InvoiceHistory.objects.create(
        user=request.user,
        company_name=invoice_info.get('company_name'),
        client_name=invoice_info.get('client_name'),
        invoice_number=invoice_number,
        issue_date=invoice_info.get('issue_date'),
        due_date=invoice_info.get('due_date'),
        total_due=total_due,
    )

    pdf_file = ContentFile(pdf)
    invoice.pdf_file.save(pdf_filename, pdf_file, save=True)

    # Clear the used session data
    keys_to_clear = ['invoice_data', 'grand_total', 'invoice_info', 'invoice_number', 'company_logo_path']
    for key in keys_to_clear:
        request.session.pop(key, None)

    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{pdf_filename}"'
    return response

@login_required
def upgrade_view(request):
    return render(request, 'invoices/upgrade.html')
    