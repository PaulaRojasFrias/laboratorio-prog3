from django.utils import timezone
from django import forms
from comisiones.models import Comision
from django.forms import DateInput, ValidationError

class ComisionForm(forms.ModelForm):
    class Meta:
        model = Comision
        fields = ('fechaDeCreacionComision', 'nroResolucionComision', 'archivoResolucion' )
        widgets = {
            'archivoResolucion': forms.ClearableFileInput(),
            'fechaDeCreacionComision': DateInput(format='%Y-%m-%d', attrs={'type': 'date'})
        }

    def clean_archivoResolucion(self):
        archivo = self.cleaned_data['archivoResolucion']
        if archivo:
            extension = archivo.name.rsplit('.', 1)[1].lower()
            if extension != 'pdf':
                raise ValidationError('El archivo seleccionado no tiene el formato PDF.')
        return archivo
    

    def clean_fechaDeCreacionComision(self):
        fecha = self.cleaned_data['fechaDeCreacionComision']
        # Verifica que la fecha de inicio sea anterior a fecha actual.
        if fecha and fecha > timezone.now().date():
            raise ValidationError(
                {'fecha_inicio': 'La Fecha de Inicio no puede ser posterior que la fecha actual'},
                code='invalido'
            )
        return fecha