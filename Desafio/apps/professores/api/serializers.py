from rest_framework import serializers
from apps.professores.models import ProfessorModel

# A classe ProfessorSerializer é responsável por serializar
# e desserializar os dados da model ProfessorModel
class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfessorModel
        fields = ('id','nome', 'email', 'formacao', 'cpf')