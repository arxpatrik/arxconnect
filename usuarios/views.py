from django.shortcuts import render, redirect
from usuarios.forms import LoginForms, CadastroForms
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib import auth


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
                return redirect('login')

    return render(request, "usuarios/login.html", {'form': form})

def cadastro(request):
    form = CadastroForms()

    if request.method == 'POST':
        form = CadastroForms(request.POST)

        if form.is_valid():

            nome = form['nome_cadastro'].value()
            email = form['email'].value()
            senha = form['senha_1'].value()
            
            #Verifica se as senhas são iguais
            if form['senha_1'].value() != form['senha_2'].value():
                messages.error(request, "As senha não coincidem")
                return redirect('cadastro')
            
            #Verifica se o username já existe
            if not User.objects.filter(username = nome).exists():

                # Cria o usuário
                usuario = User.objects.create_user(
                    username = nome,
                    email = email,
                    password = senha
                )
                usuario.save()
                return redirect('login')

    return render(request, "usuarios/cadastro.html", {'form': form})