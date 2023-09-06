from rest_framework import serializers
from apps.alunos.models import AlunoModel
#from apps.cursos.models import CursoModel

class AlunoSerializer(serializers.ModelSerializer):
    # curso = serializers.SerializerMethodField()
    nome_curso = serializers.CharField(source='curso.nome_curso', read_only=True)
    professor_curso  = serializers.CharField(source='curso.professor', read_only=True)
        
    class Meta:
        model = AlunoModel
        fields = ('id', 'nome','cpf', 'email', 'data_nascimento','curso', 'nome_curso', 'professor_curso')
    
# def get_curso(self, obj):
            
#             data = []
            
#             sections = list(CursoModel.objects.filter(id=obj.curso.id).values())
            
#             for section in sections:
#                 data.append({
#                     'Curso Escolhido': section['nome_curso'],
#                     'Professor do Curso': obj.curso.professor.nome,
#                 })
                
#             if len(data)==0:
#                 return None
#             else:
#                 return data
        