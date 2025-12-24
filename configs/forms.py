from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario

class UsuarioCreateForm(UserCreationForm):
    class Meta:

        model = Usuario
        fields = [
            "first_name",
            "last_name",
            "email",
            "telefone",
            "cpf",
            "username",
            "empresa",
            "password1",
            "password2",
        ]