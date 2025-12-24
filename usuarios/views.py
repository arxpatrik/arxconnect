from django.shortcuts import render, redirect
from usuarios.forms import LoginForms
from django.conf import settings
from django.contrib import messages
from django.contrib import auth
from django.contrib import messages


# Create your views here.

def login(request):
    form = LoginForms()

    if request.method == 'POST':
        form = LoginForms(request.POST)

        if form.is_valid():
            nome = form.cleaned_data['nome_login']
            senha = form.cleaned_data['senha']

            usuario = auth.authenticate(
                request,
                username = nome,
                password = senha
            )
            if usuario is not None:
                auth.login(request, usuario)
                return redirect('home')
            else:
                messages.warning(request, 'Usuário ou senha inválidos')
            

    return render(request, "usuarios/login.html", {'form': form})
