from django.contrib import admin

from comisiones.models import Comision, TribunalEvaluador, IntegrantesComision, IntegrantesTribunal

# Register your models here.

admin.site.register(Comision)

admin.site.register(TribunalEvaluador)

admin.site.register(IntegrantesComision)

admin.site.register(IntegrantesTribunal)