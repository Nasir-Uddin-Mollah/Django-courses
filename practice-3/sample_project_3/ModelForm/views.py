from django.shortcuts import render
from . import forms
from . import models
# Create your views here.


def modelform(request):
    if request.method == 'POST':
        form = forms.mymodelform(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = forms.mymodelform()
    return render(request, 'modelform.html', {'form': form})