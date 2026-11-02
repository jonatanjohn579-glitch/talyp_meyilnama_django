from django.urls import path
from . import views

urlpatterns = [path('', views.homework_index, name='homework_index')]
