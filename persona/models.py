from django.db import models

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

class Alumno(AbstractPersona):
    dni = models.CharField(max_length=8, unique=True)
    matricula = models.CharField(max_length=5, unique=True)
    correo = models.EmailField(max_length=254)

class Asesor(AbstractPersona):
    curriculum = models.FileField(upload_to= "archivosCurriculums") #FIJARSE COMO ES 