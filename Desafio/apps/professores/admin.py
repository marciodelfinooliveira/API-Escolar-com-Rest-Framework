from django.contrib import admin
from apps.professores.models import Professor

class Professores(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email')
    list_display_links = ('id', 'email')
    search_fields = ('formacao',)
    list_per_page = 5
    
admin.site.register(Professor, Professores)
 