from django.db import models

from nutrientes.models import Nutriente


class Recomendado(Nutriente):
    massa = models.FloatField()
    idade = models.IntegerField()

    def __str__(self):
        return self.massa

    class Meta:
        db_table = 'recomendado'
