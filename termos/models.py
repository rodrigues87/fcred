from django.core.validators import MaxLengthValidator
from django.db import models


# Create your models here.

class Termos(models.Model):
    termo = models.TextField(max_length=10000, blank=True, validators=[MaxLengthValidator(10000)])


class Aceite(models.Model):
    termo = models.ForeignKey(Termos, on_delete=models.CASCADE)
    aceite = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)
