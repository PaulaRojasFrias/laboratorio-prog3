from django.utils import timezone
from django import forms
from datetime import date
from comisiones.models import Comision, IntegrantesComision, IntegrantesTribunal, TribunalEvaluador
from django.forms import DateInput, ValidationError

class ComisionForm(forms.ModelForm):
    class Meta:
        model = Comision
        fields = ('fechaDeCreacionComision', 'nroResolucionComision', 'archivoResolucion' )
        labels = {'fechaDeCreacionComision': 'Fecha de Resolucion', 
                  'nroResolucionComision': 'Nro. Resolucion', 
                  'archivoResolucion': 'Archivo Resolucion' }
        widgets = {
            'fechaDeCreacionComision': DateInput(format='%Y-%m-%d', attrs={'type': 'date', 'class': 'campoInput'}),
            'nroResolucionComision': forms.TextInput(attrs={'type': 'number', 'class': 'campoInput'}),
            'archivoResolucion': forms.FileInput(attrs={'class': 'campoInput'})
        }

    def clean_archivoResolucion(self):
        archivo = self.cleaned_data['archivoResolucion']
        if archivo:
            extension = archivo.name.rsplit('.', 1)[1].lower()
            if extension != 'pdf':
                raise ValidationError('El archivo seleccionado no tiene el formato PDF.')
        return archivo
    

    def clean_fechaDeCreacionComision(self):
        fecha_comision = self.cleaned_data.get('fechaDeCreacionComision')
        fecha_actual = date.today()

        if fecha_comision and fecha_comision > fecha_actual:
            raise forms.ValidationError("La fecha de creación de la comisión no puede ser posterior a la fecha actual.")

        return fecha_comision
    

class IntegranteComisionForm(forms.ModelForm):
    class Meta:
        model = IntegrantesComision
        fields = ('docente', 'comision', 'fecha_alta_cs', 'fecha_baja_cs' )

        labels= {'docente': 'Docente', 
                 'comision': 'Comision', 
                 'fecha_alta_cs': 'Fecha Alta', 
                 'fecha_baja_cs': 'Fecha Baja' }
        
        widgets = {
            'docente': forms.Select(attrs={'class': 'campoInput'}),
            'comision': forms.Select(attrs={'class': 'campoInput'}), 
            'fecha_alta_cs': DateInput(format='%Y-%m-%d', attrs={'type': 'date', 'class': 'campoInput formulario__input', 'id': 'fecha_alta_cs', 'name': 'fecha_alta_cs'}),
            'fecha_baja_cs': DateInput(format='%y-%m-%d', attrs={'type': 'date', 'class': 'campoInput formulario__input', 'id': 'fecha_baja_cs', 'name': 'fecha_baja_cs'})
        }

        def clean_fecha_alta_cs(self):
            fecha_comision = self.cleaned_data.get('fecha_alta_cs')
            fecha_actual = date.today()

            if fecha_comision and fecha_comision > fecha_actual:
                raise forms.ValidationError("La fecha de incorporacion no puede ser posterior a la fecha actual.")

            return fecha_comision

        def clean_fecha_baja_cs(self):
            fecha_comision = self.cleaned_data.get('fecha_baja_cs')
            fecha_actual = date.today()

            if fecha_comision and fecha_comision > fecha_actual:
                raise forms.ValidationError("La fecha de incorporacion no puede ser posterior a la fecha actual.")

            return fecha_comision
        
        def clean(self):
            cleaned_data = super().clean()
            fecha_alta = self.cleaned_data['fecha_alta_cs']
            fecha_baja = self.cleaned_data['fecha_baja_cs']
            # Verifica que la fecha de inicio sea anterior a fecha fin.
            if fecha_baja and fecha_alta > fecha_baja:
                raise ValidationError(
                    {'fecha_alta': 'La Fecha de alta no puede ser posterior que la fecha de baja'},
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
            'archivoDisposicion': forms.ClearableFileInput(attrs={'class': 'campoInput'}),
            'fechaCreacionTribunal': DateInput(format='%Y-%m-%d', attrs={'type': 'date', 'class': 'campoInput'}),
            'proyectoTE': forms.Select(attrs={'class': 'campoInput'}),
            'nroDisposicionTribunal':forms.TextInput(attrs={'class': 'campoInput'}),
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
    
class IntegrantesTribunalForm(forms.ModelForm):
    class Meta:
        model = IntegrantesTribunal
        fields = ('docente', 'tribunal', 'fecha_alta_te', 'fecha_baja_te', 'rol' )
        labels = {'docente': 'Docente', 
                  'tribunal': 'Tribunal', 
                  'fecha_alta_te': 'Fecha Alta', 
                  'fecha_baja_te': 'Fecha Baja', 
                  'rol': 'Rol Docente',  }
        
        widgets = {
            'docente': forms.Select(),
            'tribunal': forms.Select(), 
            'fecha_alta_te': DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
            'fecha_baja_te': DateInput(format='%y-%m-%d', attrs={'type': 'date'}),
            'rol':forms.Select(choices=IntegrantesTribunal.rol_opc)
        }
