from django.db import models
from django.contrib.auth.models import User
import uuid

class InvoiceHistory(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=200, blank=True)
    client_name = models.CharField(max_length=255)
    invoice_number = models.CharField(max_length=100)
    issue_date = models.DateField()
    due_date = models.DateField()
    total_due = models.DecimalField(max_digits=10, decimal_places=2)
    pdf_file = models.FileField(upload_to='invoices/pdfs/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.invoice_number} - {self.client_name}"