from django.shortcuts import render, redirect
from . import forms
from . import models
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
# Create your views here.


class CreateAlbumView(CreateView):
    model = models.AlbumModel
    form_class = forms.AlbumForm
    template_name = 'album.html'
    success_url = reverse_lazy('homepage')


class EditAlbumView(UpdateView):
    model = models.AlbumModel
    form_class = forms.AlbumForm
    template_name = 'album.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('homepage')


class DeleteAlbumView(DeleteView):
    model = models.AlbumModel
    template_name = 'delete.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('homepage')
