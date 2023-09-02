from django.db import models

class Aluno(models.Model):
    
    nome = models.CharField(max_length=100, blank=False, null=False)
    email = models.EmailField(max_length=100, blank=False, null=False)
    data_nascimento = models.DateField(blank=False, null=False)

# Vai se associar a vários cursos
    
    def __str__(self) -> str:
        return self.nome
    

