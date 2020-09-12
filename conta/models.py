from django.db import models

from usuarios.models import Prospector


class Conta(models.Model):
    usuario = models.ForeignKey(Prospector, on_delete=models.CASCADE)
    data_expiracao = models.DateTimeField()

    def __str__(self):
        return self.usuario.usuario.first_name

    class Meta:
        verbose_name_plural = "Conta"
