from django import forms
from dictamenes.models import EvaluacionPTF_CSTF,EvaluacionPTF_TE,EvaluacionITF
class EvaluacionPTF_CSTFForm(forms.ModelForm):
    class Meta:
        model = EvaluacionPTF_CSTF
        fields = ( 'evaluadorCSTF' , 'ptf_evaluadoCSTF','fechaEvaluacionCSTF', 'informeEvaluacionCSTF','resultadoCSTF', 'observaciones')

        labels = {'resultadoCSTF': 'Resultado', 
                  'observaciones': 'Observaciones', 
                  'evaluadorCSTF': 'Comision',
                  'ptf_evaluadoCSTF': 'Proyecto',
                  'informeEvaluacionCSTF': 'Informe',
                  'fechaEvaluacionCSTF': 'Fecha Evaluacion'}
        
        widgets = {
            'resultadoCSTF': forms.Select(choices=EvaluacionPTF_CSTF.resultados_opc, attrs={'class': 'campoInput'}),
            'fechaEvaluacionCSTF': forms.DateInput(attrs={'type': 'date', 'class': 'campoInput'}),
            'evaluadorCSTF':forms.Select(attrs={'class': 'campoInput'}),
            'ptf_evaluadoCSTF':forms.Select(attrs={'class': 'campoInput'}),
            'informeEvaluacionCSTF':forms.FileInput(attrs={'class': 'campoInput'}),
            'observaciones': forms.Textarea(attrs={'class': 'campoInput'})
        }


class EvaluacionPTF_TEForm(forms.ModelForm):
    class Meta:
        model = EvaluacionPTF_TE
        fields = ( 'evaluadorTE', 'ptf_evaluadoTE', 'fechaEvaluacionTE', 'resultadoTE', 'observaciones','informeEvaluacionTE')

        labels = {'resultadoTE': 'Resultado', 
                  'observaciones': 'Observaciones', 
                  'evaluadorTE': 'Comision',
                  'ptf_evaluadoTE': 'Proyecto',
                  'informeEvaluacionTE': 'Informe',
                  'fechaEvaluacionTE': 'Fecha Evaluacion'}
        

        widgets = {
            'resultadoTE': forms.Select(choices=EvaluacionPTF_TE.resultados_opc, attrs={'class': 'campoInput'}),
            'fechaEvaluacionTE': forms.DateInput(attrs={'type': 'date', 'class': 'campoInput'}),
            'evaluadorTE':forms.Select(attrs={'class': 'campoInput'}),
            'ptf_evaluadoTE':forms.Select(attrs={'class': 'campoInput'}),
            'informeEvaluacionTE':forms.FileInput(attrs={'class': 'campoInput'}),
            'observaciones': forms.Textarea(attrs={'class': 'campoInput'})
        }

class EvaluacionITFForm(forms.ModelForm):
    class Meta:
        model = EvaluacionITF
        fields = ('resultadoITF', 'observaciones', 'evaluadorTE_ITF', 'itf_evaluadoTE', 'informeEvaluacionITF', 'fechaEvaluacionITF')
        widgets = {
            'resultadoITF': forms.Select(choices=EvaluacionITF.resultados_opc),
            'fechaEvaluacionITF': forms.DateInput(attrs={'type': 'date'})
        }