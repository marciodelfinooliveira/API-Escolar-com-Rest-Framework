from django.contrib import admin
from apps.alunos.models import AlunoModel

# A classe abaixo é usada para personalizar a aparência e o comportamento 
# da interface administrativa da model Aluno
class AlunoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'data_nascimento', 'curso','cpf', 'email',)
    list_display_links = ('id', 'cpf',)
    search_fields = ('cpf',)
    list_per_page = 10
    
admin.site.register(AlunoModel, AlunoAdmin)
 