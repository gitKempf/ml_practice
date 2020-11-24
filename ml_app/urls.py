"""
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('titanic/', views.titanic, name='titanic'),
    path('titanic_result/', views.titanic_result, name='titanic_result'),
    path('fit_fat/', views.fit_fat, name='fit_fat'),
    path('fit_fat_result/', views.fit_fat_result, name='fit_fat_result')
]
