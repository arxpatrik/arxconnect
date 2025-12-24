from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class Usuario(AbstractUser):
    telefone = models.CharField(max_length=20, blank=True)
    empresa = models.CharField(max_length=100, blank=True)
    cpf = models.CharField(
        max_length=11,
        unique=True,
    )
    def __str__(self):
        return f"{self.username} ({self.email})"