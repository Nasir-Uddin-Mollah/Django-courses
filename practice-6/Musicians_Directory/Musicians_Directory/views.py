from django.shortcuts import render
from Album.models import AlbumModel


def home(request):
    album = AlbumModel.objects.all()
    return render(request, 'home.html', {'album': album})
