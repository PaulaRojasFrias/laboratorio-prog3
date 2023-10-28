from django.utils import timezone
from django import forms
from comisiones.models import Comision, IntegrantesComision, TribunalEvaluador
from django.forms import DateInput, ValidationError

class ComisionForm(forms.ModelForm):
    class Meta:
        model = Comision
        fields = ('fechaDeCreacionComision', 'nroResolucionComision', 'archivoResolucion' )
        labels = {'fechaDeCreacionComision': 'Fecha de Resolucion', 
                  'nroResolucionComision': 'Nro. Resolucion', 
                  'archivoResolucion': 'Archivo Resolucion' }
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
                {'fecha_inicio': 'La Fecha no puede ser posterior que la fecha actual'},
                code='invalido'
            )
        return fecha
    


class IntegranteComisionForm(forms.ModelForm):
    class Meta:
        model = IntegrantesComision
        fields = ('docente', 'comision', 'fecha_alta_cs', 'fecha_baja_cs' )
        labels = {'docente': 'Docente', 
                  'comision': 'Comision', 
                  'fecha_alta_cs': 'Fecha Alta', 
                  'fecha_baja_cs': 'Fecha Baja' }
        
        widgets = {
            'docente': forms.Select(),
            'comision': forms.Select(), 
            'fecha_alta_cs': DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
            'fecha_baja_cs': DateInput(format='%y-%m-%d', attrs={'type': 'date'})
        }

        def clean_fecha_alta_cs(self):
            fecha = self.cleaned_data['fecha_alta_cs']
            # Verifica que la fecha de inicio sea anterior a fecha actual.
            if fecha and fecha > timezone.now().date():
                raise ValidationError(
                    {'fecha_inicio': 'La Fecha de Inicio no puede ser posterior que la fecha actual'},
                    code='invalido'
                )
            return fecha
        
        def clean(self):
            cleaned_data = super().clean()
            fecha_inicio = self.cleaned_data['fecha_alta_cs']
            fecha_fin = self.cleaned_data['fecha_baja_cs']
            # Verifica que la fecha de inicio sea anterior a fecha fin.
            if fecha_fin and fecha_inicio > fecha_fin:
                raise ValidationError(
                    {'fecha_inicio': 'La Fecha de alta no puede ser posterior que la fecha baja'},
                    code='invalido'
                )
            return cleaned_data



class TribunalForm(forms.ModelForm):
    class Meta:
        model = TribunalEvaluador
        fields = ('nroDisposicionTribunal', 'fechaCreacionTribunal', 'archivoDisposicion', 'proyectoTE')
        labels = {'nroDisposicionTribunal': 'Nro. Disposicion Tribunal', 
                  'fechaCreacionTribunal': 'Fecha de Disposion', 
                  'archivoDisposicion': 'Archivo Disposion', 
                  'proyectoTE': 'Proyecto'}
        widgets = {
            'archivoDisposicion': forms.ClearableFileInput(),
            'fechaCreacionTribunal': DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
            'proyectoTE': forms.Select()
        }
    
    def clean_archivoDisposicion(self):
        archivo = self.cleaned_data['archivoDisposicion']
        if archivo:
            extension = archivo.name.rsplit('.', 1)[1].lower()
            if extension != 'pdf':
                raise ValidationError('El archivo seleccionado no tiene el formato PDF.')
        return archivo
    
    def clean_fechaCreacionTribunal(self):
        fecha = self.cleaned_data['fechaCreacionTribunal']
        # Verifica que la fecha de inicio sea anterior a fecha actual.
        if fecha and fecha > timezone.now().date():
            raise ValidationError(
                {'fecha_inicio': 'La Fecha de Inicio no puede ser posterior que la fecha actual'},
                code='invalido'
            )
        return fecha