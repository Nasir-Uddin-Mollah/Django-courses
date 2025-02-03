<<<<<<< HEAD
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='homepage'),
    path('about/', views.about, name='aboutpage'),
    path('form/', views.submit_form, name='submit_form'),
    path('django_form/', views.PasswordValidationForm, name='django_form'),
]
=======
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='homepage'),
    path('about/', views.about, name='aboutpage'),
    path('form/', views.submit_form, name='submit_form'),
    path('django_form/', views.PasswordValidationForm, name='django_form'),
]
>>>>>>> af6d9f7c37900db1dbc9b7b8ef4ae50f40336f55
