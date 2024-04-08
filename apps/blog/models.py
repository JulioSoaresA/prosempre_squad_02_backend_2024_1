from django.db import models
from django.utils import formats

class Noticia(models.Model):
    foto = models.ImageField('Foto de Exibição', null=True, blank=True, upload_to='core/static/img/noticias')
    foto2 = models.ImageField('Foto de Exibição 2', null=True, blank=True, upload_to='core/static/img/noticias')
    titulo = models.CharField(verbose_name='Título', max_length=150)
    subtitulo = models.CharField(verbose_name='Subtítulo', max_length=150)
    descricao = models.TextField(verbose_name='Descrição')
    data_publicacao = models.DateField(verbose_name='Data de publicação', auto_now_add=True)
    cadastrado_por = models.CharField(verbose_name='Cadastrado por', max_length=150)

    class Meta:
        verbose_name = "Notícia"
        verbose_name_plural = "Notícias"
        db_table = 'noticia'

    def __str__(self):
        return self.titulo
