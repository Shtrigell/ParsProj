from django.urls import path, re_path

from .views import *
from .services import parse


urlpatterns = [
    path('', index, name='home'),
    path('history/', history, name = 'history'),
]