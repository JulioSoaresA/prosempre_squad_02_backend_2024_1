from django.contrib import admin
from .models import Equipe

class EquipeAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'titulo')
    list_display_links = ('id', 'nome')
    list_filter = ('nome', 'titulo')
    filter_horizontal = ()
    fieldsets = ()

admin.site.register(Equipe, EquipeAdmin)
