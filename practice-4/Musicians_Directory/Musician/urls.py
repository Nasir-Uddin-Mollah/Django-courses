from django.urls import path, include
from . import views
urlpatterns = [
    path('create/', views.CreateMusician, name='musicianpage'),
    path('edit/<int:id>', views.EditMusician, name='editmusician')
]
