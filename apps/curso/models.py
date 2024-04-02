from django.db import models
from decimal import Decimal

class Curso(models.Model):
    foto = models.ImageField('Foto de Exibição', null=True, blank=True, upload_to='core/static/img/cursos')
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

    def preco_formatado(self):
        return f'R${self.preco:.2f}'.replace('.', ',')

    def parcela_10x(self):
        preco = float(self.preco)
        return f'10x de R${(preco * 1.10) / 10:.2f}'.replace('.', ',')

    def parcela_24x(self):
        preco = float(self.preco)
        return f'24x de R${(preco * 1.12) / 24:.2f}'.replace('.', ',')

class NossaHistoria(models.Model):
    foto = models.ImageField('Foto de Exibição', null=True, blank=True, upload_to='core/static/img/nossa_historia')
    titulo = models.CharField(verbose_name='Título', max_length=150)
    descricao = models.TextField(verbose_name='Descrição')
    ativo = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Nossa História"
        verbose_name_plural = "Nossa História"
        db_table = 'nossa_historia'

    def __str__(self):
        return self.titulo

class NossosValores(models.Model):
    foto = models.ImageField('Foto de Exibição', null=True, blank=True, upload_to='core/static/img/nossos_valores')
    titulo = models.CharField(verbose_name='Título', max_length=150)
    descricao = models.TextField(verbose_name='Descrição')
    ativo = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Nossos Valores"
        verbose_name_plural = "Nossos Valores"
        db_table = 'nossos_valores'

    def __str__(self):
        return self.titulo