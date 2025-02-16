from django.urls import path
from . import views
urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('profile/passchange/', views.pass_change, name='passchange'),
    path('profile/passchange2/', views.pass_change2, name='passchange2'),
]
