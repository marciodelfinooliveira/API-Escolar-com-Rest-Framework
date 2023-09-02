from rest_framework import viewsets
from apps.cursos.api.serializers import CursoSerializer
from apps.cursos.models import Curso

class CursoViewSet(viewsets.ModelViewSet):
    
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer