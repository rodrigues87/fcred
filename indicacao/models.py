from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Indicacao(models.Model):
    prospector = models.CharField(max_length=255)
    nome_indicado = models.CharField(max_length=255)
    telefone_indicado = PhoneNumberField()
    efetivada = models.BooleanField()

    def __str__(self):
        return self.nome_indicado

    class Meta:
        verbose_name_plural = "Indicações"
