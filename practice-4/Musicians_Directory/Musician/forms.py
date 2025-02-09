from django import forms
from . models import MusicianModel


class ModelForm(forms.ModelForm):
    class Meta:
        model = MusicianModel
        fields = '__all__'
