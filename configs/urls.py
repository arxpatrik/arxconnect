from django.urls import path
from . import views

app_name = "configs"

urlpatterns = [
        path("usuarios/", views.user_manager, name='user_manager'),
        path("usuarios/novo/", views.criar_usuario, name="criar_usuario"),
    ]