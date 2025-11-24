from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Permissao(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.nome

        
class NivelAcesso(models.Model):
    nome = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nome
        
class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    ativo = models.BooleanField(default=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    nivel = models.ForeignKey('NivelAcesso', on_delete=models.SET_NULL, null=True, blank=True)
    permissoes = models.ManyToManyField('Permissao', blank=True)
    def __str__(self):
        return f"{self.user.username} ({self.user.email})"

    
class UsuarioPermissao(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='permissoes_usuario')
    permissao = models.ForeignKey(Permissao, on_delete=models.CASCADE)
    nivel = models.ForeignKey(NivelAcesso, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('usuario', 'permissao')

    def __str__(self):
        return f"{self.usuario.user.username} → {self.permissao.nome} ({self.nivel.nome})"
    