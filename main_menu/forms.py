from django import forms
from .models import ClientRequest


class ClientRequestForm(forms.ModelForm):
    class Meta:
        model = ClientRequest
        fields = '__all__'
