from django.urls import path, include
from . import views
urlpatterns = [
    path('create/', views.CreateAlbumView.as_view(), name='albumpage'),
    path('edit/<int:id>', views.EditAlbumView.as_view(), name='editalbum'),
    path('delete/<int:id>', views.DeleteAlbumView.as_view(), name='deletealbum'),
]
