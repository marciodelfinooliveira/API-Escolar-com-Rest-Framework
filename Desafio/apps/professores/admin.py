from django.contrib import admin
from apps.professores.models import ProfessorModel

class ProfessorAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'cpf', 'email','formacao', 'curso',)
    list_display_links = ('id','cpf', 'curso',)
    search_fields = ('curso','cpf',)
    list_per_page = 1
    
admin.site.register(ProfessorModel, ProfessorAdmin)
 