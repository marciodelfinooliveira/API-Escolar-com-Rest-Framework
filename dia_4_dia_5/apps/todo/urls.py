from rest_framework import routers
from apps.todo.api.viewsets import TaskViewSet
from django.urls import path, include

router = routers.DefaultRouter()
router.register('', TaskViewSet, basename='task')

urlpatterns = [
    path('', include(router.urls)),
]