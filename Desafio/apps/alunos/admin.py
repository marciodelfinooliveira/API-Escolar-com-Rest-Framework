from django.contrib import admin
from apps.alunos.models import AlunoModel

# A classe abaixo é usada para personalizar a aparência e o comportamento 
# da interface administrativa da model Aluno
class AlunoAdmin(admin.ModelAdmin):
    list_display = ('curso', 'nome', 'data_nascimento','id','cpf', 'email',)
    list_display_links = ('curso', 'cpf',)
    search_fields = ('cpf',)
    
admin.site.register(AlunoModel, AlunoAdmin)
 