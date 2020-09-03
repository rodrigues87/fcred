from django.db import models

from indicacao.models import Indicacao
from produto.models import Produto
from datetime import datetime


class Venda(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    valor = models.DecimalField(max_digits=6, decimal_places=2)
    data_efetivada = models.DateTimeField(default=datetime.now, blank=True)
    indicacao = models.ForeignKey(Indicacao, on_delete=models.CASCADE)

    def __str__(self):
        return self.produto

    class Meta:
        verbose_name_plural = "Vendas"
