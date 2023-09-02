from django.contrib import admin
from apps.cursos.models import Curso


class Cursos(admin.ModelAdmin):
    
    list_display = ('id', 'nome_curso', 'descricao', 'turno', 'nivel')
    list_display_links = ('id', 'turno')
    search_fields = ('nivel',)
    
admin.site.register(Curso, Cursos)


#class Matriculas(admin.ModelAdmin):
    
#    list_display = ('id', 'aluno', 'curso')
#    list_display_links = ('id',)
 
#admin.site.register(Matricula, Matriculas)  