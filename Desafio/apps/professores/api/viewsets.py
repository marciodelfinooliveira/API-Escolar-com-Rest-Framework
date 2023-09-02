from rest_framework import viewsets
from apps.professores.api.serializers import ProfessorSerializer
from apps.professores.models import ProfessorModel

class ProfessorViewSet(viewsets.ModelViewSet):
    
    queryset = ProfessorModel.objects.all()
    serializer_class = ProfessorSerializer