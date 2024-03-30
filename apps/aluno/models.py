from django.db import models

class Aluno(models.Model):
    foto = models.ImageField('Foto de Exibição', null=True, blank=True, upload_to='core/static/img/alunos')
    nome = models.CharField(verbose_name="Nome", max_length=150)
    curso = models.ForeignKey('curso.Curso', on_delete=models.CASCADE, verbose_name="Curso")
    ano_ingresso = models.IntegerField(verbose_name="Ano de Ingresso")
    ano_conclusao = models.IntegerField(verbose_name="Ano de Conclusão")
    descricao = models.TextField(verbose_name="Descrição")
    ativo = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Aluno"
        verbose_name_plural = "Alunos"
        db_table = 'aluno'

    def __str__(self):
        return self.nome
