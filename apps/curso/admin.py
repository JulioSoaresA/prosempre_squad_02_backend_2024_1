from django.contrib import admin
from .models import Curso, NossaHistoria, NossosValores


class CursosAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'area_conhecimento')
    list_display_links = ('id', 'nome', )
    list_filter = ('nome', 'titulacao', 'area_conhecimento')
    filter_horizontal = ()
    fieldsets = ()

class NossaHistoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo')
    list_display_links = ('id', 'titulo')
    list_filter = ('titulo', )
    filter_horizontal = ()
    fieldsets = ()

class NossosValoresAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo')
    list_display_links = ('id', 'titulo')
    list_filter = ('titulo', )
    filter_horizontal = ()
    fieldsets = ()
    
admin.site.register(Curso, CursosAdmin)
admin.site.register(NossaHistoria, NossaHistoriaAdmin)
admin.site.register(NossosValores, NossosValoresAdmin)