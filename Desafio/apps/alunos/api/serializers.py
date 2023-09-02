from rest_framework import serializers
from apps.alunos.models import Aluno

class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = ('id', 'nome', 'email', 'data_nascimento')