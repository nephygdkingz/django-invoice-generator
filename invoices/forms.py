from django import forms
from .utils import generate_invoice_number

class UploadInvoiceForm(forms.Form):
    file = forms.FileField(
        label='Upload CSV or Excel file',
        help_text='Only .csv and .xlsx files are supported',
        widget=forms.ClearableFileInput(attrs={
            'class': 'form-control mb-3',
        })
    )


class InvoiceForm(forms.Form):
    # Company Info
    company_name = forms.CharField(max_length=255, required=True)
    company_address = forms.CharField(widget=forms.Textarea, required=True)
    company_email = forms.EmailField(required=True)
    company_logo = forms.ImageField(required=False)

    # Client Info
    client_name = forms.CharField(max_length=255, required=True)
    client_address = forms.CharField(widget=forms.Textarea, required=True)
    client_email = forms.EmailField(required=False)

    # Invoice Info
    # invoice_number = forms.CharField(
    #     max_length=20,
    #     help_text="Leave blank for auto-generate",
    #     default=generate_invoice_number,
    #     editable=False,
    # )
    issue_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}), required=True
    )
    due_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}), required=True
    )

    # Dynamic fields
    notes = forms.CharField(widget=forms.Textarea, required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            widget = field.widget
            existing_classes = widget.attrs.get('class', '')

            # Add Bootstrap form-control
            widget.attrs['class'] = f'{existing_classes} form-control'.strip()

            # Add rows if the widget is a Textarea
            if isinstance(widget, forms.Textarea):
                widget.attrs['rows'] = 2 