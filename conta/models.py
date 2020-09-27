from django.db import models

from usuarios.models import User, Prospector
import string
import random
import datetime
from django.shortcuts import render, redirect
from django.contrib import messages


class Conta(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    data_expiracao = models.DateTimeField()
    codigo_verificador = models.CharField(max_length=30)
    codigo_verificador_tentado = models.CharField(max_length=30,blank=True,null=True)

    def __str__(self):
        return self.usuario.first_name

    def verificar_conta(self, request):
        if self.codigo_verificador == self.codigo_verificador_tentado:
            self.usuario.validado = True
            self.usuario.save()
            return redirect('/')
        else:
            messages.error(request, "Código informado está incorreto")
            return redirect('/login/verificar')

    def codigo_verificador_generator(self):
        self.codigo_verificador = ''.join(
            random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(6))

    def criar_conta(self):
        self.codigo_verificador_generator()
        self.data_expiracao = datetime.datetime.now() + datetime.timedelta(days=365)
        self.usuario.enviar_email(self)
        self.save()

    class Meta:
        verbose_name_plural = "Conta"
