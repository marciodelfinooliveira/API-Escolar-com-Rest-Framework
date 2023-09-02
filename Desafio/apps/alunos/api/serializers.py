from rest_framework import serializers
from apps.alunos.models import AlunoModel

class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlunoModel
        fields = ('id', 'nome','cpf', 'email', 'data_nascimento', 'curso')