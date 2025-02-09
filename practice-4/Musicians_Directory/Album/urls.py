from django.urls import path, include
from . import views
urlpatterns = [
    path('create/', views.CreateAlbum, name='albumpage'),
    path('edit/<int:id>', views.EditAlbum, name='editalbum'),
    path('delete/<int:id>', views.DeleteAlbum, name='deletealbum')
]
