from django import forms
from dictamenes.models import EvaluacionPTF_CSTF,EvaluacionPTF_TE,EvaluacionITF
class EvaluacionPTF_CSTFForm(forms.ModelForm):
    class Meta:
        model = EvaluacionPTF_CSTF
        fields = ('resultadoCSTF', 'observaciones', 'evaluadorCSTF' ,'ptf_evaluadoCSTF','informeEvaluacionCSTF','fechaEvaluacionCSTF')
        widgets = {
            'resultadoCSTF': forms.Select(choices=EvaluacionPTF_CSTF.resultados_opc),
            'fechaEvaluacionCSTF': forms.DateInput(attrs={'type': 'date'})
        }


class EvaluacionPTF_TEForm(forms.ModelForm):
    class Meta:
        model = EvaluacionPTF_TE
        fields = ('resultadoTE', 'observaciones', 'evaluadorTE', 'ptf_evaluadoTE', 'informeEvaluacionTE', 'fechaEvaluacionTE')
        widgets = {
            'resultadoTE': forms.Select(choices=EvaluacionPTF_TE.resultados_opc),
            'fechaEvaluacionTE': forms.DateInput(attrs={'type': 'date'})
        }

class EvaluacionITFForm(forms.ModelForm):
    class Meta:
        model = EvaluacionITF
        fields = ('resultadoITF', 'observaciones', 'evaluadorTE_ITF', 'itf_evaluadoTE', 'informeEvaluacionITF', 'fechaEvaluacionITF')
        widgets = {
            'resultadoITF': forms.Select(choices=EvaluacionITF.resultados_opc),
            'fechaEvaluacionITF': forms.DateInput(attrs={'type': 'date'})
        }