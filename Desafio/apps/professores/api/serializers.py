from rest_framework import serializers
from apps.professores.models import Professor

class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = ('id', 'nome', 'email', 'formacao')