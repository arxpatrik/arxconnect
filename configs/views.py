from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UsuarioCreateForm

User = get_user_model()

@login_required(login_url='login')

def user_manager(request):
    if request.method == 'POST':
        form = UsuarioCreateForm(request.POST)
        if form.is_valid():
            print("Form Ok")
            usuario = form.save(commit=False)
            usuario.save()

            messages.success(request, 'Usuário criado com sucesso!')
            return redirect('configs:user_manager')
    else:
        form = UsuarioCreateForm()
        print(form.errors)

    listar = User.objects.all()

    return render(request, "user_manager.html", {
        'listar': listar,
        'form': form,
    })
