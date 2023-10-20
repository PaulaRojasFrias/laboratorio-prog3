from django.db import models

from proyecto_trabajo_final.models import ProyectoFinal,Movimientos


from comisiones.models import IntegrantesComision,IntegrantesTribunal,TribunalEvaluador
# Create your models here.

class EvaluacionPTF_CSTF(models.Model):
    evaluacion = (
        ('aprobado', 'Aprobado'),
        ('observado', 'Observado'),
        ('rechazado', 'Rechazado')
    )
    evaluador = models.ForeignKey(IntegrantesComision, on_delete= models.CASCADE)
    ptf_evaluado = models.ForeignKey(ProyectoFinal, on_delete= models.CASCADE)
    movimiento_registrado = models.ForeignKey(Movimientos, on_delete= models.CASCADE)
    archivo_evaluacion =models.FileField(null=True, blank=True)
    observaciones =models.CharField(max_length=256)
class EvaluacionPTF_TE(models.Model):
    evaluacion = (
        ('aprobado', 'Aprobado'),
        ('observado', 'Observado'),
        ('rechazado', 'Rechazado')
    )
    evaluador = models.ForeignKey(IntegrantesTribunal, on_delete=models.CASCADE)
    ptf_evaluado = models.ForeignKey(ProyectoFinal, on_delete=models.CASCADE)
    movimiento_registrado = models.ForeignKey(Movimientos, on_delete=models.CASCADE)
    archivo_evaluacion = models.FileField(null=True, blank=True)
    observaciones = models.CharField(max_length=256)

class EvaluacionITF(models.Model):
    evaluacion = (
        ('aprobado', 'Aprobado'),
        ('observado', 'Observado'),
        ('rechazado', 'Rechazado')
    )
    evaluador = models.ForeignKey(IntegrantesTribunal, on_delete=models.CASCADE)
    """itf_evaluado = models.ForeignKey(InformeProyectoFinal, on_delete=models.CASCADE)"""
    movimiento_registrado = models.ForeignKey(Movimientos, on_delete=models.CASCADE)
    archivo_evaluacion = models.FileField(null=True, blank=True)
    observaciones = models.CharField(max_length=256)



class DefensaOral(models.Model):
    evaluacion = (
        ('aprobado', 'Aprobado'),
        ('desaprobado', 'Desaprobado'),
    )
    tribunalEvaluador = models.ForeignKey(TribunalEvaluador, on_delete=models.CASCADE)
    """itf_evaluado = models.ForeignKey(InformeProyectoFinal, on_delete=models.CASCADE)"""
    movimiento_registrado = models.ForeignKey(Movimientos, on_delete=models.CASCADE)

