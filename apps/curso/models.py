from django.db import models

class Curso(models.Model):
    foto = models.FileField('Foto de Exibição', null=True, blank=True, upload_to='core/static/img/cursos')
    nome = models.CharField(verbose_name='Nome', max_length=150)
    area_conhecimento = models.CharField(verbose_name='Área de Conhecimento', max_length=100)
    descricao = models.TextField(verbose_name='Descrição')
    titulacao = models.CharField(verbose_name='Titulação', max_length=100)
    carga_horaria = models.IntegerField(verbose_name='Carga Horária')
    nota = models.DecimalField(verbose_name='Nota', max_digits=2, decimal_places=1)
    preco = models.DecimalField(verbose_name='Preço', max_digits=7, decimal_places=2)
    modalidade = models.CharField(verbose_name='Modalidade', max_length=100)
    ativo = models.BooleanField(default=True)


    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"
        db_table = 'curso'

    def __str__(self):
        return self.nome