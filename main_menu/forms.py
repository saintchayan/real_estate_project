from django import forms
from .models import ClientRequest


class ClientRequestForm(forms.ModelForm):
    class Meta:
        model = ClientRequest
        fields = '__all__'
        labels = {
            'name': 'Your name',
            'phone': 'Phone',
            'email': 'Your email',
            'message': 'Your message',
        }
        error_messages = {
            'name': {
                'max_length': 'Input value is too long',
                'min_length': 'Your name must include at least 4 symbols',
                'required': 'Name field cannot be blank',
            }
        }
