from django import forms
from .models import ClientRequest


class ClientRequestForm(forms.ModelForm):
    class Meta:
        model = ClientRequest
        fields = '__all__'
        label = {
            'name': 'Your Name',
            'phone': 'Phone number',
            'email': 'Your email (optional)',
            'message': 'Your message',
        }
