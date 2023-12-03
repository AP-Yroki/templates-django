from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('about/', views.about),
    path('contact/', views.contact,
         {'phone': '+79379837733', 'social_network': 'https://github.com/AP-Yroki',
          'address': 'Банановая 38', 'link': 'ссылка на что-то'}, name='contact'),
    path('contacts/', views.contacts, name='contacts'),
    path('form/', views.form),
]
