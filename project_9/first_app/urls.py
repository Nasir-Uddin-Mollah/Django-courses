from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.set_session),
    path('get/', views.get_session),
    path('del/', views.del_session),
]
