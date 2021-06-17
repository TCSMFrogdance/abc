from django.urls import path
from .views import Home, About, Story

urlpatterns = [
    path('', Home, name='home'),
    path('story/', Story, name='story'),
    path('about/', About, name='about'),
]