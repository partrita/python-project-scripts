from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from . import views

urlpatterns = [
    path('',views.index, name="index"),
    path('accounts/login/',LoginView.as_view(), name="login"),
    path('accounts/logout/',LogoutView.as_view(), name='logout'),
    path('accounts/register/',views.register, name='register'),
    path('user/',views.user, name="user")
]