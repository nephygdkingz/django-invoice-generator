from django.urls import path
from . import views

app_name = 'invoices'

urlpatterns = [
    path('upload/', views.upload_invoice_view, name='upload'),
    path('preview/', views.preview_invoice_view, name='preview'),
]