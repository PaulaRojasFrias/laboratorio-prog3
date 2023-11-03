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
            'nombre': forms.TextInput(attrs={'class': 'campoInput'}),
            'apellido': forms.TextInput(attrs={'class': 'campoInput'}),
            'correo': forms.EmailInput(attrs={'class': 'campoInput'}),
            'dni': forms.TextInput(attrs={'class': 'campoInput'}),
            'matricula': forms.TextInput(attrs={'class': 'campoInput'}),
        }

class AsesorForm(forms.ModelForm):
    class Meta:
        model = Asesor
        fields = ('nombre', 'apellido', 'cuil', 'curriculum')
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'cuil': forms.TextInput(attrs={'class': 'form-control'}),
            'curriculum': forms.ClearableFileInput(attrs={'multiple': False}),

        }
