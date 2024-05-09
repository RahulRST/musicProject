from django.urls import path

from musicApp import views

urlpatterns = [
    path('', views.login),
    path('home', views.home)
]