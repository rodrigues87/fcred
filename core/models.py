from django.db import models

from nutrientes.models import Nutriente


class Alimento(Nutriente):
    nome = models.CharField(max_length=255, blank=True, null=True)
    category = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.nome

    class Meta:
        db_table = 'alimento'
