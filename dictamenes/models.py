from django.db import models

from proyecto_trabajo_final.models import InformeTF, ProyectoFinal,Movimientos


from comisiones.models import Comision, IntegrantesComision,IntegrantesTribunal,TribunalEvaluador
# Create your models here.

class EvaluacionPTF_CSTF(models.Model):
    resultados_opc = (
        ('aprobado', 'Aprobado'),
        ('observado', 'Observado'),
        ('rechazado', 'Rechazado')
    )
    resultadoCSTF = models.CharField(max_length=256, choices= resultados_opc)
    observaciones = models.CharField(max_length=256, null=True, blank=True)
    evaluadorCSTF = models.ForeignKey(Comision, on_delete= models.CASCADE)
    ptf_evaluadoCSTF = models.OneToOneField(ProyectoFinal, on_delete= models.CASCADE) #PREGUNTAR A LA PROFE
    informeEvaluacionCSTF =models.FileField(null=True, blank=True, upload_to='archivosDictamenes/')
    fechaEvaluacionCSTF = models.DateField(auto_now=False)
    #movimiento_registrado = models.ForeignKey(Movimientos, on_delete= models.CASCADE) 

class EvaluacionPTF_TE(models.Model):
    resultados_opc = (
        ('aprobado', 'Aprobado'),
        ('observado', 'Observado'),
        ('rechazado', 'Rechazado')
    )
    resultadoTE = models.CharField(max_length=256, choices= resultados_opc)
    observaciones = models.CharField(max_length=256, null=True, blank=True)
    evaluadorTE = models.OneToOneField(TribunalEvaluador, on_delete=models.CASCADE)#PREGUNTAR A LA PROFE
    ptf_evaluadoTE = models.OneToOneField(ProyectoFinal, on_delete=models.CASCADE)#PREGUNTAR A LA PROFE
    informeEvaluacionTE = models.FileField(null=True, blank=True, upload_to='archivosDictamenes/')
    fechaEvaluacionTE = models.DateField(auto_now=False)
    #movimiento_registrado = models.ForeignKey(Movimientos, on_delete=models.CASCADE)

class EvaluacionITF(models.Model):
    resultados_opc = (
        ('aprobado', 'Aprobado'),
        ('observado', 'Observado'),
        ('rechazado', 'Rechazado')
    )
    resultadoITF = models.CharField(max_length=256, choices= resultados_opc)
    observaciones = models.CharField(max_length=256)
    evaluadorTE_ITF = models.OneToOneField(TribunalEvaluador, on_delete=models.CASCADE)#PREGUNTAR A LA PROFE
    itf_evaluadoTE = models.OneToOneField(InformeTF, on_delete=models.CASCADE)
    informeEvaluacionITF = models.FileField(null=True, blank=True, upload_to='archivosDictamenes/')
    fechaEvaluacionITF = models.DateField(auto_now=False)
    #movimiento_registrado = models.ForeignKey(Movimientos, on_delete=models.CASCADE)
    
class DefensaOral(models.Model):
    fechaDefensa = models.DateField(auto_now=False)
    notaObtenida = models.IntegerField()
