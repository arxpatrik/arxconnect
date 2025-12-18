from django.shortcuts import render
from .models import Pessoa
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')
def pendencias_view(request):
    pessoas = Pessoa.objects.all()
    return render (request, 'pendencias.html', {"pessoas": pessoas })

def Salvar(request):
    vnome = request.POST.get("nome")
    Pessoa.objects.create(nome=vnome)
    pessoas = Pessoa.objects.all()
    pendencias_view(request)
    return render (request, 'pendencias.html', {"pessoas": pessoas })


def editar(request, id):
    pessoa = get_object_or_404(Pessoa, id=id)

    if request.method == 'POST':
        pessoa.nome = request.POST.get('nome')
        pessoa.save()
        return redirect('pendencias:lista')  # ajuste se necessário

    return render(request, 'pendencias/editar.html', {
        'pessoa': pessoa
    })