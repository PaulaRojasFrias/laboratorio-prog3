from django import forms
from django.utils import timezone
from django.forms import DateInput, ValidationError
from proyecto_trabajo_final.models import PTF_Integrantes, ProyectoFinal

class ProyectoForm(forms.ModelForm):
    class Meta:
        model = ProyectoFinal
        fields = ('titulo', 'descripcion', 'fechaPresentacion', 'proyectoFinal' )
        labels = {'titulo': 'Titulo', 
                  'descripcion': 'Descripcion', 
                  'fechaPresentacion': 'Fecha de Presentacion',
                  'proyectoFinal': 'Archivo Proyecto'  }
        
        widgets = {
            'proyectoFinal': forms.ClearableFileInput(),
            'fechaPresentacion': DateInput(format='%Y-%m-%d', attrs={'type': 'date'})
        }
    
    def clean_proyectoFinal(self):
        archivo = self.cleaned_data['proyectoFinal']
        if archivo:
            extension = archivo.name.rsplit('.', 1)[1].lower()
            if extension != 'pdf':
                raise ValidationError('El archivo seleccionado no tiene el formato PDF.')
        return archivo
    
    def clean_fechaPresentacion(self):
        fecha = self.cleaned_data['fechaPresentacion']
        # Verifica que la fecha de inicio sea anterior a fecha actual.
        if fecha and fecha > timezone.now().date():
            raise ValidationError(
                {'fecha_inicio': 'La Fecha no puede ser posterior que la fecha actual'},
                code='invalido'
            )
        return fecha
    



    
class IntegranteProyectoForm(forms.ModelForm):
    class Meta:
        model = PTF_Integrantes
        fields = ('proyectoFinal', 'alumnos', 'fechaAltaAlumno', 'fechaBajaAlumno', 'certificadoAnalitico')
        
        labels ={'proyectoFinal': 'Proyecto Final', 
                  'alumnos': 'Alumno', 
                  'fechaAltaAlumno': 'Fecha Alta', 
                  'fechaBajaAlumno': 'Fecha Baja',
                  'certificadoAnalitico': 'Certificado Analitico',}
        
        widgets = {
            'proyectoFinal': forms.Select(),
            'alumnos': forms.Select(), 
            'fechaAltaAlumno': DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
            'fechaBajaAlumno': DateInput(format='%y-%m-%d', attrs={'type': 'date'}),
            'certificadoAnalitico': forms.ClearableFileInput(),
        }

        def clean_fechaAltaAlumno(self):
            fecha = self.cleaned_data['fecha_alta_cs']
            # Verifica que la fecha de inicio sea anterior a fecha actual.
            if fecha and fecha > timezone.now().date():
                raise ValidationError(
                    {'fecha_inicio': 'La Fecha de Inicio no puede ser posterior que la fecha actual'},
                    code='invalido'
                )
            return fecha
        
        def clean_certificadoAnalitico(self):
            archivo = self.cleaned_data['certificadoAnalitico']
            if archivo:
                extension = archivo.name.rsplit('.', 1)[1].lower()
                if extension != 'pdf':
                    raise ValidationError('El archivo seleccionado no tiene el formato PDF.')
            return archivo
        
        def clean(self):
            cleaned_data = super().clean()
            fecha_inicio = self.cleaned_data['fechaAltaAlumno']
            fecha_fin = self.cleaned_data['fechaBajaAlumno']
            # Verifica que la fecha de inicio sea anterior a fecha fin.
            if fecha_fin and fecha_inicio > fecha_fin:
                raise ValidationError(
                    {'fecha_inicio': 'La Fecha de alta no puede ser posterior que la fecha baja'},
                    code='invalido'
                )
            return cleaned_data