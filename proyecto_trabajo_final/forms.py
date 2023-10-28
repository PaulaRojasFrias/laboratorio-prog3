from django import forms
from django.utils import timezone
from django.forms import DateInput, ValidationError
from proyecto_trabajo_final.models import AsesorPTF, PTF_Integrantes, ProyectoFinal, TutoresPTF

#<<<<<<<<<<<<<<<<<<<<<<<<< PROYECTO TRABAJO FINAL >>>>>>>>>>>>>>>>>>>>>>
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
    


#<<<<<<<<<<<<<<<<<<<<<<<<< ALUMNOS QUE CONFORMAN LOS PROYECTOS  >>>>>>>>>>>>>>>>>>>>>>
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
            fecha = self.cleaned_data['fechaAltaAlumno']
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
        


#<<<<<<<<<<<<<<<<<<<<<<<<< TUTORES QUE CONFORMAN LOS PROYECTOS  >>>>>>>>>>>>>>>>>>>>>>
class TutorForm(forms.ModelForm):
    class Meta:
        model = TutoresPTF
        fields = ('docente', 'fechaAltaTutor', 'fechaBajaTutor', 'notaAceptacion', 'rol_tutor', 'proyecto')
        
        labels ={'proyecto': 'Proyecto Final', 
                  'docente': 'Docente', 
                  'fechaAltaTutor': 'Fecha Alta', 
                  'fechaBajaTutor': 'Fecha Baja',
                  'notaAceptacion': 'Nota Aceptacion',
                  'rol_tutor': 'Rol del Tutor',}
        
        widgets = {
            'proyecto': forms.Select(),
            'docente': forms.Select(), 
            'fechaAltaTutor': DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
            'fechaBajaTutor': DateInput(format='%y-%m-%d', attrs={'type': 'date'}),
            'notaAceptacion': forms.ClearableFileInput(),
            'rol_tutor': forms.Select(choices=TutoresPTF.rol_docente)
        }

        def clean_fechaAltaTutor(self):
            fecha = self.cleaned_data['fechaAltaTutor']
            # Verifica que la fecha de inicio sea anterior a fecha actual.
            if fecha and fecha > timezone.now().date():
                raise ValidationError(
                    {'fecha_inicio': 'La Fecha de Inicio no puede ser posterior que la fecha actual'},
                    code='invalido'
                )
            return fecha
        
        def clean_notaAceptacion(self):
            archivo = self.cleaned_data['notaAceptacion']
            if archivo:
                extension = archivo.name.rsplit('.', 1)[1].lower()
                if extension != 'pdf':
                    raise ValidationError('El archivo seleccionado no tiene el formato PDF.')
            return archivo
        
        def clean(self):
            cleaned_data = super().clean()
            fecha_inicio = self.cleaned_data['fechaAltaTutor']
            fecha_fin = self.cleaned_data['fechaBajaTutor']
            # Verifica que la fecha de inicio sea anterior a fecha fin.
            if fecha_fin and fecha_inicio > fecha_fin:
                raise ValidationError(
                    {'fecha_inicio': 'La Fecha de alta no puede ser posterior que la fecha baja'},
                    code='invalido'
                )
            return cleaned_data
        
class AsesorPTFForm(forms.ModelForm):
    class Meta:
        model = AsesorPTF
        fields = ('asesor', 'fechaAltaAsesor', 'fechaBajaAsesor', 'notaAceptacion', 'proyecto')
        
        labels ={'proyecto': 'Proyecto Final', 
                  'asesor': 'Asesor', 
                  'fechaAltaAsesor': 'Fecha Alta', 
                  'fechaBajaAsesor': 'Fecha Baja',
                  'notaAceptacion': 'Nota Aceptacion',}
        
        widgets = {
            'proyecto': forms.Select(),
            'asesor': forms.Select(), 
            'fechaAltaAsesor': DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
            'fechaBajaAsesor': DateInput(format='%y-%m-%d', attrs={'type': 'date'}),
            'notaAceptacion': forms.ClearableFileInput(),
        }

        def clean_fechaAltaAsesor(self):
            fecha = self.cleaned_data['fechaAltaAsesor']
            # Verifica que la fecha de inicio sea anterior a fecha actual.
            if fecha and fecha > timezone.now().date():
                raise ValidationError(
                    {'fecha_inicio': 'La Fecha de Inicio no puede ser posterior que la fecha actual'},
                    code='invalido'
                )
            return fecha
        
        def clean_notaAceptacion(self):
            archivo = self.cleaned_data['notaAceptacion']
            if archivo:
                extension = archivo.name.rsplit('.', 1)[1].lower()
                if extension != 'pdf':
                    raise ValidationError('El archivo seleccionado no tiene el formato PDF.')
            return archivo
        
        def clean(self):
            cleaned_data = super().clean()
            fecha_inicio = self.cleaned_data['fechaAltaAsesor']
            fecha_fin = self.cleaned_data['fechaBajaAsesor']
            # Verifica que la fecha de inicio sea anterior a fecha fin.
            if fecha_fin and fecha_inicio > fecha_fin:
                raise ValidationError(
                    {'fecha_inicio': 'La Fecha de alta no puede ser posterior que la fecha baja'},
                    code='invalido'
                )
            return cleaned_data
        
