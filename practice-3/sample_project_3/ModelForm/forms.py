from django import forms
from django.core.validators import validate_ipv4_address
from .models import mymodel

class mymodelform(forms.ModelForm):
    class Meta:
        model = mymodel
        fields = '__all__'
    