from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LessonViewSet, BellPeriodViewSet

router = DefaultRouter()
router.register(r'lessons', LessonViewSet)
router.register(r'bells', BellPeriodViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
