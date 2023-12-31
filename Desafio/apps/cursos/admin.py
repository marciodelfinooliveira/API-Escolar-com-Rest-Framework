from django.contrib import admin
from apps.cursos.models import CursoModel

# A classe abaixo é usada para personalizar a aparência e o comportamento 
# da interface administrativa da model Curso
class CursoAdmin(admin.ModelAdmin):
    
    list_display = ('id', 'nome_curso', 'codigo_curso', 'descricao', 'carga_horaria', 'turno', 'nivel', 'professor',)
    list_display_links = ('id', 'turno', 'carga_horaria',)
    search_fields = ('codigo_curso', 'nivel', 'carga_horaria',)
    list_per_page = 5
    
admin.site.register(CursoModel, CursoAdmin)
