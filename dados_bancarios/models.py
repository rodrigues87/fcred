from django.core.validators import MaxValueValidator
from django.db import models


class Dados_bancarios(models.Model):
    numero_banco = models.PositiveIntegerField(validators=[MaxValueValidator(999)])
    nome_banco = models.CharField(max_length=150)
    agencia = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    conta = models.PositiveIntegerField(validators=[MaxValueValidator(99999999999)])
    digito_conta = models.PositiveIntegerField(validators=[MaxValueValidator(9)])


    CORRENTE = 'CR'
    POUPANCA = 'PO'
    PAGAMENTO = 'PG'

    TIPO_CONTA_CHOICES = [
        ('CR', 'Corrente'),
        ('PO', 'Poupança'),
        ('PG', 'Pagamento'),
        ('PX', 'PIX')

    ]

    tipo_de_conta = models.CharField(
        max_length=2,
        choices=TIPO_CONTA_CHOICES,
        default=CORRENTE,
    )

    def __str__(self):
        return self.conta.__str__()
