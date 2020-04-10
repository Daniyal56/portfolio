from django.contrib import admin
from django.urls import path, include
from myapp import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('projects/', views.projects, name='projects'),
    path('contact/', views.contact, name='contact'),
    path('home/', views.index, name='home'),
    path('About/', views.about, name='about'),
    path('Projects/', views.projects, name='projects'),
    path('Contact/', views.contact, name='contact'),
    path('Home/', views.index, name='home'),
]
