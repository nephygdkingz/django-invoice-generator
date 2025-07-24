from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse

class InvoiceAppTest(TestCase):
    def test_home_redirects_unauthenticated(self):
        """Test that unauthenticated user is redirected from home"""
        response = self.client.get(reverse('account:dashboard'))  # Uses the named URL
        self.assertEqual(response.status_code, 302)  # Should redirect to login

    def test_dashboard_requires_login(self):
        """Test that dashboard requires login"""
        response = self.client.get(reverse('account:dashboard'))
        self.assertEqual(response.status_code, 302)
        self.assertIn('/account/login/', response.url)  # Ensure it redirects to login