from rest_framework import serializers
from apps.cursos.models import CursoModel

class CursoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CursoModel
        fields = ('id', 'nome_curso',  'codigo_curso', 'descricao','carga_horaria', 'turno', 'nivel', 'professor', 'alunos')