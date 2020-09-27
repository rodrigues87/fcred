from cpf_field.models import CPFField
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils.translation import ugettext_lazy as _
from datetime import date

from dados_bancarios.models import Dados_bancarios
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import render, redirect


class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    """User model."""

    username = None
    email = models.EmailField(_('email address'), unique=True)
    imagem_url = models.CharField(max_length=600, blank=True, null=True)
    validado = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.first_name

    def logar(self, request):
        try:
            user = authenticate(username=self.email, password=self.password)
            if user is not None:
                login(request, user)

                if user.validado:
                    return redirect('/')
                else:
                    return redirect('/usuarios/login/verificar')
            else:
                messages.error(request, "Usuário e senha inválido. Favor tentar novamente.")
                return redirect('/usuarios/login')

        except User.DoesNotExist:
            messages.error(request, "Usuário não existe")
            return redirect('/usuarios/login')

    def criar_usuario(self, request):
        try:
            user = User.objects.get(email=self.email)
            messages.error(request, "Usuário já existe")
            return None

        except User.DoesNotExist:
            self.save()
            return self

    def enviar_email(self, conta):
        send_mail('E-mail de Cofirmação', 'Seu código de confirmação: ' + conta.codigo_verificador,
                  'contato@fcred.com.br', ['pedroh.mix@gmail.com'], fail_silently=False, )


class Prospector(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    cpf = CPFField('cpf')
    telefone_celular = PhoneNumberField()
    dados_bancarios = models.ForeignKey(Dados_bancarios, on_delete=models.CASCADE)

    def __str__(self):
        return self.usuario.first_name

    class Meta:
        verbose_name_plural = "Prospectores"
