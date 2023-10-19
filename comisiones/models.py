from django.db import models

from persona.models import Docente

class Comision(models.Model):
    fechaDeCreacionComision = models.DateField(auto_now_add=False)
    nroResolucionComision = models.CharField(max_length=30, unique=True)
    archivoResolucion = models.FileField()
    class Meta:
       ordering = ['fechaDeCreacionComision']


class TribunalEvaluador(models.Model):
    nroDisposicionTribunal = models.CharField(max_length=50, unique = True)
    fechaCreacionTribunal = models.DateField(auto_now_add=False)
    archivoDisposicion = models.FileField()
    class Meta:
       ordering = ['fechaCreacionTribunal']

class IntegrantesComision(models.Model):
    docente = models.OneToOneField(Docente, on_delete=models.CASCADE)
    comision = models.OneToOneField(Comision, on_delete=models.CASCADE)
    fecha_alta_cs = models.DateField(auto_now_add=False)
    fecha_baja_cs = models.DateField(auto_now_add=False)
    class Meta:
       ordering = ['fecha_alta_cs']

class IntegrantesTribunal(models.Model):
    rol_opc = (
        ('presidente', 'Presidente'),
        ('vocal_titular',  'Vocal Titular'),
        ('vocal_secundario', 'Vocal Secundario')
    )
    docente = models.ForeignKey(Docente, on_delete= models.CASCADE)
    tribunal = models.ForeignKey(TribunalEvaluador, on_delete= models.CASCADE)
    rol = models.CharField(max_length=16, choices= rol_opc)
    fecha_alta_te = models.DateField(auto_now_add=False)
    fecha_baja_te = models.DateField(auto_now_add=False)
    class Meta:
       ordering = ['fecha_alta_te']
