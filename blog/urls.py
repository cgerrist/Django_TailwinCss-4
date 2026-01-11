from django.shortcuts import render
from django.views.generic import TemplateView
from .views import blog

# Create your views here.
from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog, name='blog'),
]

