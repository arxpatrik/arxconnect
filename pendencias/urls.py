
from django.urls import path
from . import views
from .views import Salvar
from .views import editar


app_name = "pendencias"
urlpatterns = [
    path("pendencias/", views.pendencias_view, name="pendencias"),
    path('Salvar/', views.Salvar, name="Salvar"),
    path('editar/<int:id>', views.editar, name="editar"),
]