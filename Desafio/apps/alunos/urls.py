from rest_framework import routers
from apps.alunos.api.viewsets import AlunoViewSet
from django.urls import path, include

#define as rotas associadas às operações que podem ser 
# realizadas com o app "Aluno"

router = routers.DefaultRouter()
router.register('', AlunoViewSet, basename='Aluno')

urlpatterns = [
    path('',include(router.urls)),
]