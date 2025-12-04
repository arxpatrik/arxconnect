from django.shortcuts import render
from .models import Pessoa

# Create your views here.

def pendencias_view(request):
    pessoas = Pessoa.objects.all()
    return render (request, 'pendencias.html', {"pessoas": pessoas })

def SalvaTeste(request):
    vnome = request.POST.get("nome")
    Pessoa.objects.create(nome=vnome)
    pessoas = Pessoa.objects.all()
    pendencias_view(request)
    return render (request, 'pendencias.html', {"pessoas": pessoas })

def editar(request, id):
    Pessoa = Pessoa.objects.get(id=id)
    return render (request, "editar.html", {"pessoa": Pessoa})