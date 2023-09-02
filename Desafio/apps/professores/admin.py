from django.contrib import admin
from apps.professores.models import ProfessorModel

class ProfessorAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'cpf', 'email','formacao',)
    list_display_links = ('id','cpf',)
    search_fields = ('cpf',)
    list_per_page = 1
    
admin.site.register(ProfessorModel, ProfessorAdmin)
 