from rest_framework import serializers
from apps.professores.models import ProfessorModel

class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfessorModel
        fields = ('id', 'nome', 'email', 'formacao', 'curso', 'cpf')