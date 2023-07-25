from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('history/', history, name = 'history'),
    path('pars/', pars)
]