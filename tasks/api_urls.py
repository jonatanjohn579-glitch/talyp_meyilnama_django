from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet, TaskCategoryViewSet, SubTaskViewSet

router = DefaultRouter()
router.register(r'items', TaskViewSet)
router.register(r'categories', TaskCategoryViewSet)
router.register(r'subtasks', SubTaskViewSet)

urlpatterns = [path('', include(router.urls))]
