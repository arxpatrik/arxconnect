from django.db import models

# Create your models here.

class Permissao(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.nome
    
class nivel_acesso(models.Model):
    nome = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nome
        
class usuario(models.Model):
    username = models.CharField(max_length=50, unique=True)
    nome_completo = models.CharField(max_length=120, unique=True)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    ativo = models.BooleanField(default=True)
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nome_completo} ({self.username})"
    
class usuario_permissao(models.Model):
    usuario = models.ForeignKey(usuario, on_delete=models.CASCADE, related_name='usuario_permissao')