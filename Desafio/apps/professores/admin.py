from django.contrib import admin
from apps.professores.models import ProfessorModel

# A classe abaixo é usada para personalizar a aparência e o comportamento 
# da interface administrativa da model Professor
class ProfessorAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'cpf', 'email','formacao',)
    list_display_links = ('id','cpf',)
    search_fields = ('cpf',)
    list_per_page = 5
    
admin.site.register(ProfessorModel, ProfessorAdmin)
 