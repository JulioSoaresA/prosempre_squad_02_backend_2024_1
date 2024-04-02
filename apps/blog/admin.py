from django.contrib import admin
from .models import Noticia

class NoticiaAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'data_publicacao')
    list_display_links = ('id', 'titulo', 'data_publicacao')
    list_filter = ('titulo', 'data_publicacao')
    filter_horizontal = ()
    fieldsets = ()

admin.site.register(Noticia, NoticiaAdmin)
