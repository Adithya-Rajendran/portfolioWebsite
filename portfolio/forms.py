from django import forms
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberInternationalFallbackWidget


class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Your Name'
        })
    )

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'email@domain.com'
        })
    )

    phone = PhoneNumberField(
        region="US",
        widget=PhoneNumberInternationalFallbackWidget(attrs={
            'class': 'form-control',
            'placeholder': '+1 (555) 555-5555'}
        ),
        required=False
    )

    message = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'style': 'height: 10rem;',
            'placeholder': 'Your Message'
        })
    )
