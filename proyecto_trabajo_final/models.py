from django.db import models

from persona.models import Alumno, Docente, Asesor


# Create your models here.

class ProyectoFinal(models.Model):
    titulo = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=250)
    fechaPresentacion = models.DateField()
    proyectoFinal = models.FileField()
    
    def _str_(self):
        return f'{self.titulo}'

class InformeTF(models.Model):
    archivoITF = models.FileField()
    fechaPresentacion = models.DateField()
    proyectoTF = models.OneToOneField(ProyectoFinal, on_delete=models.CASCADE)

class AsesorPTF(models.Model):
    asesor= models.ForeignKey(Asesor, on_delete=models.SET_NULL, null=True, blank=True, related_name='proyectos_asesor')
    fechaAltaAsesor = models.DateField()
    fechaBajaAsesor = models.DateField(null=True, blank=True)
    notaAceptacion = models.FileField(null=True, blank=True)

class TutoresPTF(models.Model):
    rol_docente = (
        ('codirector', 'Codirector'),
        ('director', 'Director'),
    )
    docente = models.ForeignKey(Docente, on_delete=models.SET_NULL, null=True, blank=True, related_name='proyectos_tutores')
    fechaAltaTutor = models.DateField()
    fechaBajaTutor = models.DateField(null=True, blank=True)
    notaAceptacion = models.FileField(null=True, blank=True)
    rol_tutor = models.CharField(max_length=50, choices=rol_docente)

class Movimientos(models.Model):
    proyectoFinal = models.OneToOneField(ProyectoFinal, on_delete=models.SET_NULL, null=True, blank=True)
    estado_opc = (
        ('aceptado', 'Aceptado'),
        ('rechazado', 'Rechazado'),
        ('observado', 'Observado'),
    )
    estado = models.CharField(max_length=50, choices=estado_opc)
    movimientos_opc = (
        ('presentacion ptf', 'Presentación PTF'),
        ('pase a la cstf', 'Pase a la CSTF'),
        ('dictamen de la cstf sobre el formato del ptf', 'Dictamen de la CSTF sobre el formato del PTF'),
        ('pase al te', 'Pase al TE'),
        ('dictamen tribunal evaluador sobre evaluación ptf', 'Dictamen tribunal evaluador sobre evaluación PTF'),
        ('presentación borrador informe final', 'Presentación borrador Informe final'),
        ('dictamen tribunal evaluador sobre borrador', 'dictamen tribunal evaluador sobre borrador'),
    )
    tipoMovimiento = models.CharField(max_length=50, choices=movimientos_opc)
    observacion = models.CharField(max_length=50,null=True, blank=True)
    fechaMovimiento = models.DateField()
    archivoAsociado = models.FileField(null=True, blank=True)
    fechaVencimiento = models.DateField(null=True, blank=True)

class PTF_Integrantes(models.Model):
    proyectoFinal = models.ForeignKey(ProyectoFinal, on_delete=models.SET_NULL, null=True, blank=True)
    alumnos = models.ForeignKey(Alumno,on_delete=models.CASCADE ,related_name='proyectos')
    fechaAltaAlumno = models.DateField(null=True, blank=True)
    fechaBajaAlumno = models.DateField(null=True, blank=True)
    certificadoAnalitico = models.FileField()
