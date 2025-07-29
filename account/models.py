from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_paid = models.BooleanField(default=False)
    company_name = models.CharField(max_length=255, blank=True)
    company_address = models.TextField(blank=True)
    company_email = models.EmailField(blank=True)
    company_logo = models.ImageField(upload_to='logos/', null=True, blank=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"