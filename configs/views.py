from django.shortcuts import render
from .models import Permissao, NivelAcesso
from django.http import HttpResponse

# Create your views here.

def user_manager(request):
    return render(request, "user_manager.html")

def criar_usuario(request):
    if request.method == 'POST':
        dados = request.POST.dict()
        r = f"""
        Método: {request.method}<br>
        Dados recebidos: <br>
        {dados}
        """
        return HttpResponse(r)
    else:
        return HttpResponse('GET')