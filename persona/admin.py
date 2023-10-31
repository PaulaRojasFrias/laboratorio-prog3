from django.contrib import admin
from django.contrib.auth.models import Permission
from persona.models import Docente, Alumno, Asesor


# Register your models here.
class AlumnoAdmin(admin.ModelAdmin):
    model = Alumno
    permission = (
        ("permiso_alumno", "Permiso alumno"),
    )


admin.site.register(Docente)

admin.site.register(Alumno)

admin.site.register(Asesor)

admin.site.register(Permission)
