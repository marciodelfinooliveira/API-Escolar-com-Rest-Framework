from rest_framework import routers
from apps.alunos.api.viewsets import AlunoViewSet
from django.urls import path, include

router = routers.DefaultRouter()
router.register('', AlunoViewSet, basename='Aluno')


urlpatterns = [
    path('', include(router.urls)),
]