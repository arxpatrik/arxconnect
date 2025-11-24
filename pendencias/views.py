from django.shortcuts import render
from .models import Pessoa
# Create your views here.

def pendencias_view(request):
    pessoas = Pessoa.objects.all()
    return render (request, 'pendencias.html')




