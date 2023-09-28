from django.urls import path, re_path

from .views import *
from .services import parse


urlpatterns = [
    path('', index, name='home'),
    path('history/', ParsLinkHistory.as_view(), name='history'),
    path('login/', LoginUser.as_view(), name='login'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('logout/', logout_user, name='logout')
]