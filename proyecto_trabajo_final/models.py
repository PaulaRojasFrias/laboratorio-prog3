from django.db import models

from persona.models import Alumno, Docente

# Create your models here.


class ProyectoFinal(models.Model):
    id = models.CharField(primary_key=True, max_length=8, unique=True)
    titulo = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=250)
    fechaPresentacion = models.DateField()
    proyectoFinal = models.FileField()
    notaAceptacionDirector = models.FileField()
    director = models.OneToOneField(Docente, on_delete=models.SET_NULL, null=True, related_name='proyectos_director')
    coDirector = models.ForeignKey(Docente, on_delete=models.SET_NULL, null=True, blank=True, related_name='proyectos_co_director')
    asesor= models.OneToOneField(Docente, on_delete=models.SET_NULL, null=True, blank=True, related_name='proyectos_asesor')
    fechaAltaDirector = models.DateField()
    fechaBajaDirector = models.DateField(null=True, blank=True)
    
    def _str_(self):
            return f'{self.titulo}'


class Movimientos(models.Model):
    proyectoFinal = models.OneToOneField(ProyectoFinal, on_delete=models.SET_NULL, null=True, blank=True)
    estado = models.CharField(max_length=50)
    fechaMovimiento = models.DateField()
    archivoAsociado = models.FileField(null=True, blank=True)
    tipoMovimiento = models.CharField(max_length=50)
    fechaVencimiento = models.DateField(null=True, blank=True)
    fechaCulminacion = models.DateField(null=True, blank=True)


class PTF_Integrantes(models.Model):
    proyectoFinal = models.OneToOneField(ProyectoFinal, on_delete=models.SET_NULL, null=True, blank=True)
    alumnos = models.ForeignKey(Alumno, on_delete= models.CASCADE)
    fechaAltaAlumno = models.DateField(null=True, blank=True)
    fechaBajaAlumno = models.DateField(null=True, blank=True)
    certificadoAnalitico = models.FileField()
