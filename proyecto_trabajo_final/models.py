from django.db import models

from persona.models import Alumno, Docente


# Create your models here.


class InformeTrabajoFinal(models.Model):
    borrador = models.FileField()
    fechaPresentacion = models.DateField()

class EstadoProyectoFinal(models.Model):
    estado= models.CharField(max_length=50)
    fechaMovimiento= models.DateField()
    archivoAsociado=  models.FileField()
    tipoMovimiento= models.CharField(max_length=50)

class ProyectoFinal(models.Model):
    titulo = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=250)
    fechaPresentacion = models.DateField()
    proyectoFinal = models.FileField()
    certificadoAnalitico= models.FileField()
    notaAceptacionDirector= models.FileField()
    curriculumVitaeAsesor= models.FileField()
    alumnos = models.ManyToManyField(Alumno, related_name='trabajos')
    docenteDirector= models.ForeignKey(Docente, on_delete=models.SET_NULL, null=True, related_name='trabajos_dirigidos')
    asesor= models.ForeignKey(Docente, on_delete=models.SET_NULL, null=True, related_name='trabajos_asesorados')
    fechaAltaDirector= models.DateField()
    fechaBajaDirector= models.DateField(null=True, blank=True)
    informe = models.OneToOneField( InformeTrabajoFinal, on_delete=models.SET_NULL, null=True, blank=True)
    estado= models.OneToOneField(  EstadoProyectoFinal, on_delete=models.SET_NULL, null=True, blank=True)


    def __str__(self):
        return self.titulo

