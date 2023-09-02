from rest_framework import viewsets
from apps.cursos.api.serializers import CursoSerializer
from apps.cursos.models import CursoModel

class CursoViewSet(viewsets.ModelViewSet):
    
    queryset = CursoModel.objects.all()
    serializer_class = CursoSerializer