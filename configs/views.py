from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Usuario
from django.contrib.auth import get_user_model

# Create your views here.

User = get_user_model()

@login_required(login_url='login')

def user_manager(request):
    usuarios = User.objects.all()
    return render(request, "user_manager.html", {
        'listar':usuarios
    })