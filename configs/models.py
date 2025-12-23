from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class Usuario(AbstractUser):
    telefone = models.CharField(max_length=20, blank=True)
    empresa = models.CharField(max_length=100, blank=True)
    cargo = models.CharField(max_length=50, blank=True)
    ativo= models.BooleanField(default=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    cpf = models.CharField(
        max_length=11,
        unique=True,
    )
    def __str__(self):
        return f"{self.username} ({self.email})"