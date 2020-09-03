from django.db import models


class Produto(models.Model):
    nome = models.CharField(max_length=255)
    comissao = models.IntegerField()

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = "produtos"
