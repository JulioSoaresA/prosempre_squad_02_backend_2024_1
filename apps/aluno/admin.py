from django.contrib import admin
from .models import Aluno


class AlunosAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'curso')
    list_display_links = ('id', 'nome', )
    list_filter = ('nome', 'curso')
    filter_horizontal = ()
    fieldsets = ()

admin.site.register(Aluno, AlunosAdmin)
