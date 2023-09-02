from rest_framework import viewsets
from apps.alunos.api.serializers import AlunoSerializer
from apps.alunos.models import AlunoModel

class AlunoViewSet(viewsets.ModelViewSet):
    
    queryset = AlunoModel.objects.all()
    serializer_class = AlunoSerializer