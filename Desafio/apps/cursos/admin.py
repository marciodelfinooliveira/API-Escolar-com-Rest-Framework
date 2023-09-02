from django.contrib import admin
from apps.cursos.models import Curso


class Cursos(admin.ModelAdmin):
    
    list_display = ('id', 'nome_curso', 'descricao', 'carga_horaria', 'turno', 'nivel')
    list_display_links = ('id', 'turno', 'carga_horaria')
    search_fields = ('nivel', 'carga_horaria')
    
admin.site.register(Curso, Cursos)


#class Matriculas(admin.ModelAdmin):
    
#    list_display = ('id', 'aluno', 'curso')
#    list_display_links = ('id',)
 
#admin.site.register(Matricula, Matriculas)  