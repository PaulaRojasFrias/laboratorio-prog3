from django.contrib import admin

from dictamenes.models import EvaluacionPTF_CSTF, EvaluacionPTF_TE, EvaluacionITF, DefensaOral

# Register your models here.

admin.site.register(EvaluacionPTF_CSTF)

admin.site.register(EvaluacionPTF_TE)

admin.site.register(EvaluacionITF)

admin.site.register(DefensaOral)