from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from usuarios.models import Prospector


class Indicacao(models.Model):
    prospector = models.ForeignKey(Prospector, on_delete=models.CASCADE)
    nome_indicado = models.CharField(max_length=255)
    telefone_indicado = PhoneNumberField()
    efetivada = models.BooleanField()
    autorizado = models.BooleanField()
    descricao = models.CharField(max_length=255)

    def __str__(self):
        return self.nome_indicado

    class Meta:
        verbose_name_plural = "Indicações"
