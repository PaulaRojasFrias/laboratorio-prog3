from django.db import models

from persona.models import Docente
from proyecto_trabajo_final.models import ProyectoFinal

class Comision(models.Model):
    fechaDeCreacionComision = models.DateField(auto_now_add=False)
    nroResolucionComision = models.CharField(max_length=30, unique=True)
    archivoResolucion = models.FileField(upload_to='archivosComisiones/')
    class Meta:
       ordering = ['fechaDeCreacionComision']
    def __str__(self):
        return f'Resolución {self.nroResolucionComision} - Año {self.fechaDeCreacionComision.year}'

class TribunalEvaluador(models.Model):
    nroDisposicionTribunal = models.CharField(max_length=50, unique = True)
    fechaCreacionTribunal = models.DateField(auto_now_add=False)
    archivoDisposicion = models.FileField(upload_to='archivosComisiones/')
    proyectoTE = models.OneToOneField(ProyectoFinal, on_delete=models.CASCADE)
    class Meta:
       ordering = ['fechaCreacionTribunal']

    def __str__(self):
        return f'Proyecto: {self.proyectoTE.titulo} - Disposición {self.nroDisposicionTribunal}'

class IntegrantesComision(models.Model):
    docente = models.ForeignKey(Docente, on_delete=models.CASCADE)
    comision = models.ForeignKey(Comision, on_delete=models.CASCADE)
    fecha_alta_cs = models.DateField(auto_now_add=False)
    fecha_baja_cs = models.DateField(auto_now_add=False, null=True, blank=True)
    class Meta:
       ordering = ['fecha_alta_cs']
    
    def __str__(self):
        return f'{self.docente.apellido}, {self.docente.nombre} - Resolución {self.comision.nroResolucionComision}'

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
    fecha_baja_te = models.DateField(auto_now_add=False, null=True, blank=True)
    class Meta:
       ordering = ['fecha_alta_te']

    def __str__(self):
        return f'{self.docente.apellido}, {self.docente.nombre} - Disposición {self.tribunal.nroDisposicionTribunal}'
