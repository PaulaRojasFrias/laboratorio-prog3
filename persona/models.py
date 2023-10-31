from django.db import models
from django.contrib.auth.models import Permission

# Create your models here.
class AbstractPersona(models.Model):
    nombre = models.CharField(max_length=70)
    apellido = models.CharField(max_length=70)

    class Meta:
        abstract = "true"
        ordering = ('apellido', 'nombre')

    def __str__(self):
        return f'{self.apellido}{self.nombre}'
 

class Docente(AbstractPersona):
    cuil = models.CharField(max_length=11, unique=True)

    class Meta:
        permissions = [
            ("permiso_cstf", "Permiso CSTF"),
            ("permiso_te", "Permiso TE"),
        ]


class Alumno(AbstractPersona):
    dni = models.CharField(max_length=8, unique=True)
    matricula = models.CharField(max_length=5, unique=True) #Pueden ser dos?
    correo = models.EmailField(max_length=254)

    class Meta:
        permissions = [
            ("permiso_alumno", "Permiso alumno"),
        ]

class Asesor(AbstractPersona):
    cuil = models.CharField(max_length=11, unique=True) #modificado
    curriculum = models.FileField(upload_to='persona/')

