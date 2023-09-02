from django.db import models

class Professor(models.Model):
    
    FORMACAO = (
        ( 'G', 'Graduação'),
        ( 'M', 'Mestrado'),
        ( 'D', 'Doutorado'),
    )
    
    nome = models.CharField(max_length=100, blank=False, null=False)
    email = models.EmailField(max_length=100, blank=False, null=False)
    formacao = models.CharField(max_length=1, choices=FORMACAO, blank=False, null=False, default='G')
    
# Vai se associar a vários cursos
    
    def __str__(self) -> str:
        return self.nome

