from django.test import TestCase
from django.contrib.auth.models import User

class InvoiceAppTest(TestCase):
    def test_home_redirects_unauthenticated(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 302)  # Redirects to login

    def test_dashboard_requires_login(self):
        response = self.client.get('/dashboard/')
        self.assertEqual(response.status_code, 302)