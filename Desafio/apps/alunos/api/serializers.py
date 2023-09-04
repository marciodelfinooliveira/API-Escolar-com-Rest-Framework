from rest_framework import serializers
from apps.alunos.models import AlunoModel

# A classe ProfessorSerializer é responsável por serializar
# e desserializar os dados da model AlunoSerializer
class AlunoSerializer(serializers.ModelSerializer):
    curso = serializers.SerializerMethodField()    
    class Meta:
        model = AlunoModel
        fields = ('id', 'nome','cpf', 'email', 'data_nascimento', 'curso',)
        
    def get_curso(self, obj):
        curso_id = obj.curso
        return curso_id.professor.nome