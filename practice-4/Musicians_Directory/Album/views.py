from django.shortcuts import render, redirect
from . import forms
from . import models
# Create your views here.


def CreateAlbum(request):
    if request.method == 'POST':
        form = forms.AlbumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = forms.AlbumForm()
    return render(request, 'album.html', {'form': form})


def EditAlbum(request, id):
    album = models.AlbumModel.objects.get(pk=id)
    form = forms.AlbumForm(instance=album)
    if request.method == 'POST':
        form = forms.AlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    return render(request, 'album.html', {'form': form})


def DeleteAlbum(request, id):
    album = models.AlbumModel.objects.get(pk=id)
    album.delete()
    return redirect('homepage')
