
from django.urls import path
from . import views


app_name = "pendencias"
urlpatterns = [
    path("pendencias/", views.pendencias_view, name="pendencias")
]