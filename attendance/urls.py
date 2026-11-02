from django.urls import path
from . import views

urlpatterns = [path('', views.attendance_index, name='attendance_index')]
