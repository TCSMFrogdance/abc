from django.urls import path
from .views import Home, About, Contact

urlpatterns = [
    path('', Home, name='home'),
    path('contact/', Contact, name='contact'),
    path('about/', About, name='about'),
]