from rest_framework import routers
from apps.alunos.api.viewsets import AlunoViewSet
from apps.cursos.api.viewsets import CursoViewSet
from apps.professores.api.viewsets import ProfessorViewSet
from django.urls import path, include

router = routers.DefaultRouter()
router.register('alunos', AlunoViewSet, basename='Alunos')
router.register('cursos', CursoViewSet, basename='Cursos')
router.register('professores', ProfessorViewSet, basename='Professores')

urlpatterns = [
    path('', include(router.urls)),

]
