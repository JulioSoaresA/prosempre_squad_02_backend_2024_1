from django.db import models


class Contato(models.Model):
    assunto = models.CharField(verbose_name='Assunto', max_length=155)
    mensagem = models.TextField(verbose_name="Mensagem", max_length=255)
    nome = models.CharField(verbose_name="Nome", max_length=150)
    email = models.EmailField(verbose_name="Email", max_length=200)

    class Meta:
        verbose_name = "Contato"
        db_table = 'contato'

    def __str__(self):
        return self.nome
