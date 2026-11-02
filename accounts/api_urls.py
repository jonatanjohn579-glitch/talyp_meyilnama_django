from django.urls import path
from . import api_views

urlpatterns = [
    path('login/', api_views.api_login, name='api_auth_login'),
    path('register/', api_views.api_register, name='api_auth_register'),
    path('me/', api_views.api_me, name='api_auth_me'),
]
