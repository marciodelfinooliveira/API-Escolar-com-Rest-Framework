from rest_framework import serializers
from apps.cursos.models import CursoModel

# A classe ProfessorSerializer é responsável por serializar
# e desserializar os dados da model CursoSerializer
class CursoSerializer(serializers.ModelSerializer):
    professor_curso  = serializers.CharField(source='professor.nome', read_only=True)

    class Meta:
        model = CursoModel
        fields = ('id', 'nome_curso', 'codigo_curso', 'descricao', 'carga_horaria', 'turno', 'nivel', 'professor', 'professor_curso')
