from django.db import models

from persona.models import Docente

# Create your models here.
class ComisionDeSeguimiento(models.Model):
    fechaDeCreacionComision = models.DateField()
    nroResolucionComision = models.CharField(max_length=30, unique=True)
    docentesComision = models.ForeignKey(Docente, on_delete= models.CASCADE)
    
    class Meta:
        ordering = ['fechaDeCreacionComision']


class TribunalEvaluador(models.Model):
    rol_opc = (
        ('presidente', 'Presidente'),
        ('vocal_titular',  'Vocal Titular'),
        ('vocal_secundario', 'Vocal Secundario')
    )

    nroDisposicionTribunal = models.CharField(max_length=50, unique = True)
    fechaCreacionTribunal = models.DateField(auto_now_add=False)
    docentesTribunal = models.ManyToManyField(Docente)
    rol = models.CharField(max_length=16, choices= rol_opc)
    

    class Meta:
        ordering = ['fechaCreacionTribunal']