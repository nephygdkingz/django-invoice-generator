from django.urls import path
from . import views

app_name = 'invoices'

urlpatterns = [
    path('upload/', views.upload_invoice_view, name='upload'),
    path('preview/', views.preview_invoice_view, name='preview'),
    path('download-pdf/', views.download_invoice_pdf_view, name='download_pdf'),
]