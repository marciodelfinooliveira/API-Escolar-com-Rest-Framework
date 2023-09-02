from rest_framework import viewsets
from apps.alunos.api.serializers import AlunoSerializer
from apps.alunos.models import Aluno

class AlunoViewSet(viewsets.ModelViewSet):
    
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer