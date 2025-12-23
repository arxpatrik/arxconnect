from django.urls import path
from . import views

app_name = "configs"

urlpatterns = [
        path("users/", views.user_manager, name='user_manager'),
    ]