from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from usuarios.models import Prospector


class Indicacao(models.Model):
    prospector = models.ForeignKey(Prospector, on_delete=models.CASCADE)
    nome_indicado = models.CharField(max_length=255)
    telefone_indicado = PhoneNumberField()
    efetivada = models.BooleanField(blank=True,null=True)
    autorizado = models.BooleanField(blank=True,null=True)
    descricao = models.CharField(max_length=255,blank=True,null=True)
    data_indicacao = models.DateTimeField(auto_now_add=True, blank=True)

    EM_ANDAMENTO = 'EA'
    FECHADO = 'FC'
    EFETIVADO = 'EF'
    RECUSADO = 'RC'
    STATUS_CHOICES = [
        (EM_ANDAMENTO, 'Em andamento'),
        (FECHADO, 'Fechado'),
        (EFETIVADO, 'Efetivado'),
        (RECUSADO, 'Recusado'),
    ]
    status = models.CharField(
        max_length=2,
        choices=STATUS_CHOICES,
        default=EM_ANDAMENTO,
    )

    def __str__(self):
        return self.prospector.usuario.first_name

    class Meta:
        verbose_name_plural = "Indicações"
