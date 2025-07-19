from django import forms

class UploadInvoiceForm(forms.Form):
    file = forms.FileField(
        label='Upload CSV or Excel file',
        help_text='Only .csv and .xlsx files are supported',
        widget=forms.ClearableFileInput(attrs={
            'class': 'form-control mb-3',
        })
    )