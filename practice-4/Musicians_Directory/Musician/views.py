from django.shortcuts import render, redirect
from . import forms
from . import models
# Create your views here.


def CreateMusician(request):
    if request.method == 'POST':
        form = forms.ModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = forms.ModelForm()
    return render(request, 'musician.html', {'form': form})


def EditMusician(request, id):
    musician = models.MusicianModel.objects.get(pk=id)
    form = forms.ModelForm(instance=musician)
    if request.method == 'POST':
        form = forms.ModelForm(request.POST, instance=musician)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    return render(request, 'musician.html', {'form': form})
