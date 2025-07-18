from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "password1", "password2")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Add 'form-control' class to each widget
        for field_name, field in self.fields.items():
            existing_classes = field.widget.attrs.get('class', '')
            # Add both 'form-control' and 'mb-3' classes
            classes = f"{existing_classes} form-control mb-3".strip()
            field.widget.attrs['class'] = classes

            placeholders = {
                'username': 'Enter username',
                'password1': 'Enter password',
                'password2': 'Confirm password',
            }
            if field_name in placeholders:
                field.widget.attrs['placeholder'] = placeholders[field_name]


class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control mb-4',
            'placeholder': 'Username',
            'autofocus': True,
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Password',
        })
    )
