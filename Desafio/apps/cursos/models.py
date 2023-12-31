from django.db import models
from apps.professores.models import ProfessorModel

class CursoModel(models.Model):
    
    TURNO = (
        ('M', 'Manhã'),
        ('T', 'Tarde'),
        ('N', 'Noite'),
    )
    
    NIVEL = (
        ('B', 'Básico'),
        ('I', 'Intermediário'),
        ('A', 'Avançado'),
    )
    
    CARGA_HORARIA = (
        ('45', '45 Horas'),
        ('60', '60 Horas'),
        ('90', '90 Horas'),
    )
    
    # Declaração das colunas da tabela do banco de dados de Cursos
    
    id = models.AutoField(primary_key=True, auto_created=True)    
    nome_curso = models.CharField(max_length=150, blank=False, null=False)
    codigo_curso = models.CharField(max_length=6, blank=False, null=False, unique=True)
    carga_horaria = models.CharField(max_length=2, choices=CARGA_HORARIA, blank=False, null=False)
    descricao = models.CharField(max_length=500, blank=False, null=False)
    turno = models.CharField(max_length=1, choices=TURNO, blank=False, null=False)
    nivel = models.CharField(max_length=1, choices=NIVEL, blank=False, null=False, default='B')          
    professor = models.ForeignKey(ProfessorModel, on_delete=models.CASCADE, blank=False, null=True)
    
    def __str__(self) -> str:
        return self.nome_curso