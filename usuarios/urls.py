from django.urls import path
from usuarios.views import login
from . import views
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('login/', login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout')
]