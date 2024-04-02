from django.db import models

class Equipe(models.Model):
    foto = models.FileField('Foto de Exibição', null=True, blank=True, upload_to='core/static/img/sobre')
    descricao = models.TextField(verbose_name='Descrição')
    titulo = models.TextField(verbose_name="Título", max_length=255)
    nome = models.CharField(verbose_name="Nome", max_length=150)

    class Meta:
        verbose_name = "Equipe"
        db_table = 'equipe'

    def __str__(self):
        return self.nome