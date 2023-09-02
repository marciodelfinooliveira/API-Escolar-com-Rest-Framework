from django.contrib import admin
from apps.alunos.models import AlunoModel

class AlunoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'data_nascimento', 'curso','cpf', 'email',)
    list_display_links = ('id', 'cpf',)
    search_fields = ('cpf',)
    list_per_page = 1
    
admin.site.register(AlunoModel, AlunoAdmin)
 