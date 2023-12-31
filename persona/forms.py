from django import forms
from .models import Docente, Alumno, Asesor

class DocenteForm(forms.ModelForm):
    class Meta:
        model = Docente
        fields = ('nombre','apellido','cuil','correo','crear_usuario')
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'campoInput'}),
            'apellido': forms.TextInput(attrs={'class': 'campoInput'}),
            'cuil': forms.TextInput(attrs={'class': 'campoInput'}),
            'correo': forms.EmailInput(attrs={'class': 'campoInput'}),
            'crear_usuario': forms.CheckboxInput(attrs={'class': 'campoInput'}),
        }


class AlumnoForm(forms.ModelForm):
    class Meta:
        model = Alumno
        fields = ('nombre', 'apellido', 'dni','matricula','correo',)
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'campoInput formulario__input', 'id': 'inputNombre', 'name': 'nombre'}),
            'apellido': forms.TextInput(attrs={'class': 'campoInput formulario__input', 'id': 'inputApellido', 'name': 'apellido'}),
            'correo': forms.EmailInput(attrs={'class': 'campoInput formulario__input', 'id': 'inputCorreo', 'name': 'correo'}),
            'dni': forms.TextInput(attrs={'class': 'campoInput formulario__input', 'id': 'inputDNI', 'name': 'dni'}),
            'matricula': forms.TextInput(attrs={'class': 'campoInput formulario__input', 'id': 'inputMatricula', 'name': 'matricula'}),
        }

class AsesorForm(forms.ModelForm):
    class Meta:
        model = Asesor
        fields = ('nombre', 'apellido', 'cuil', 'curriculum',)
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'campoInput'}),
            'apellido': forms.TextInput(attrs={'class': 'campoInput'}),
            'cuil': forms.TextInput(attrs={'class':'campoInput'}),
            'curriculum': forms.ClearableFileInput(attrs={'multiple': False, 'class':'campoInput'}),

        }
