from rest_framework import serializers
from apps.alunos.models import AlunoModel

class AlunoSerializer(serializers.ModelSerializer):
    curso_nome_curso = serializers.CharField(source='curso.nome_curso', read_only=True)
    class Meta:
        model = AlunoModel
        fields = ('id', 'nome','cpf', 'email', 'data_nascimento', 'curso', 'curso_nome_curso')