from .models import Security
from django import forms


class SecurityForm(forms.ModelForm):
    class Meta:
        model = Security
        fields = ('__all__')