
from django.urls import path
from . import views
from .views import SalvaTeste


app_name = "pendencias"
urlpatterns = [
    path("pendencias/", views.pendencias_view, name="pendencias"),
    path('SalvaTeste/', views.SalvaTeste, name="SalvaTeste"),
    path('editar/<int:id>'  , views.editar, name="editar"),
]