from django.contrib import admin
from .models import Usuario
from django.contrib.auth.admin import UserAdmin


# Register your models here.
@admin.register(Usuario)

class UsuarioAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Cargos', {
            'fields': ('cargo','cpf'),
        }),
    )
    pass

