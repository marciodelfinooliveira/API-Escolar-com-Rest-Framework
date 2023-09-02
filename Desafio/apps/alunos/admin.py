from django.contrib import admin
from apps.alunos.models import Aluno

class Alunos(admin.ModelAdmin):
    list_display = ('id', 'nome', 'data_nascimento')
    list_display_links = ('id', 'nome')
    search_fields = ('email',)
    list_per_page = 5
    
admin.site.register(Aluno, Alunos)
 