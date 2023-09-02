from rest_framework import serializers
from apps.cursos.models import Curso

class CursoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Curso
        fields = ('id', 'nome_curso', 'descricao','carga_horaria', 'turno', 'nivel')