from django.contrib import admin
from django.contrib.auth.models import Permission
from usuarios.models import Administrador


# Register your models here.
class AdministradorAdmin(admin.ModelAdmin):
    model = Administrador
    permission = (
        ("permiso_administrador", "Permiso administrador"),
    )


admin.site.register(Administrador, AdministradorAdmin)
