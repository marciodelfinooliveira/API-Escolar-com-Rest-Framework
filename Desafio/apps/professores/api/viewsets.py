from rest_framework import viewsets
from apps.professores.api.serializers import ProfessorSerializer
from apps.professores.models import Professor

class ProfessorViewSet(viewsets.ModelViewSet):
    
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer