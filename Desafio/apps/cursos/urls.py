from rest_framework import routers
from apps.cursos.api.viewsets import CursoViewSet
from django.urls import path, include

#define as rotas associadas às operações que podem ser 
# realizadas com o app "Curso"

router = routers.DefaultRouter()
router.register('', CursoViewSet, basename='Curso')

urlpatterns = [
    path('', include(router.urls)),
]