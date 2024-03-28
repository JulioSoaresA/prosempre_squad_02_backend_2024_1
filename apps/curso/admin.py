from django.contrib import admin
from .models import Curso


class CursosAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'area_conhecimento')
    list_display_links = ('id', 'nome', )
    list_filter = ('nome', 'titulacao', 'area_conhecimento')
    filter_horizontal = ()
    fieldsets = ()

admin.site.register(Curso, CursosAdmin)