from django.urls import path
from . import views

urlpatterns = [
    path('', views.schedule_index, name='schedule_index'),
]
