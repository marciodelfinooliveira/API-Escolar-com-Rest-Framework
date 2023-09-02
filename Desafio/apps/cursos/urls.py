from rest_framework import routers
from apps.cursos.api.viewsets import CursoViewSet
from django.urls import path, include

router = routers.DefaultRouter()
router.register('', CursoViewSet, basename='Curso')

urlpatterns = [
    path('', include(router.urls)),
]