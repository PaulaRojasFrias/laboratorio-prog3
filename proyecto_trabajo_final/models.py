from django.db import models
from django.utils import timezone
from persona.models import Alumno, Docente, Asesor
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class ProyectoFinal(models.Model):
    titulo = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=250)
    fechaPresentacion = models.DateField()
    proyectoFinal = models.FileField(upload_to='archivosPTF/')
    
    def __str__(self):
        return f'{self.titulo}'

class InformeTF(models.Model):
    proyectoTF = models.OneToOneField(ProyectoFinal, on_delete=models.CASCADE)
    archivoITF = models.FileField(upload_to='archivosPTF/')
    fechaPresentacion = models.DateField()
    

class AsesorPTF(models.Model):
    proyecto = models.ForeignKey(ProyectoFinal, on_delete=models.SET_NULL, null=True, blank=True)
    asesor= models.ForeignKey(Asesor, on_delete=models.SET_NULL, null=True, blank=True, related_name='proyectos_asesor')
    fechaAltaAsesor = models.DateField()
    fechaBajaAsesor = models.DateField(null=True, blank=True)
    notaAceptacion = models.FileField(null=True, blank=True, upload_to='archivosPTF/')

class TutoresPTF(models.Model):
    rol_docente = (
        ('codirector', 'Codirector'),
        ('director', 'Director'),
    )
    docente = models.ForeignKey(Docente, on_delete=models.SET_NULL, null=True, blank=True, related_name='proyectos_tutores')
    proyecto = models.ForeignKey(ProyectoFinal, on_delete=models.SET_NULL, null=True, blank=True)
    fechaAltaTutor = models.DateField()
    fechaBajaTutor = models.DateField(null=True, blank=True)
    notaAceptacion = models.FileField(null=True, blank=True, upload_to='archivosPTF/')
    rol_tutor = models.CharField(max_length=50, choices=rol_docente)
    

class Movimientos(models.Model):
    proyecto = models.OneToOneField(ProyectoFinal, on_delete=models.SET_NULL, null=True, blank=True)
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
    tipoMovimiento = models.CharField(max_length=50, choices=movimientos_opc, null=True, blank=True)
    observacion = models.CharField(max_length=50,null=True, blank=True)
    fechaMovimiento = models.DateField()
    archivoAsociado = models.FileField(null=True, blank=True, upload_to='archivosPTF/')
    fechaVencimiento = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'{self.proyecto.titulo} - {self.get_tipoMovimiento_display()}'

@receiver(post_save, sender=ProyectoFinal)
def crear_movimiento(sender, instance, created, **kwargs):
    if created:
        # Crea un nuevo movimiento asociado al proyecto final y asigna el archivo asociado
        movimiento = Movimientos.objects.create(
            proyecto=instance,
            tipoMovimiento='presentacion ptf',
            fechaMovimiento=timezone.now(),
            archivoAsociado=instance.proyectoFinal  # Asigna el archivo asociado del proyecto final al movimiento
        )

class PTF_Integrantes(models.Model):
    proyectoFinal = models.ForeignKey(ProyectoFinal, on_delete=models.SET_NULL, null=True, blank=True)
    alumnos = models.ForeignKey(Alumno,on_delete=models.CASCADE, related_name='proyectos')
    fechaAltaAlumno = models.DateField(null=True, blank=True)
    fechaBajaAlumno = models.DateField(null=True, blank=True)
    certificadoAnalitico = models.FileField(upload_to='archivosPTF/')

    def __str__(self):
        return f'{self.proyectoFinal.titulo} - {self.alumnos.nombre} {self.alumnos.apellido}'
