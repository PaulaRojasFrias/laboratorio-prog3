from django import forms
from .models import Docente, Alumno, Asesor

class DocenteForm(forms.ModelForm):
    class Meta:
        model = Docente
        fields = ('nombre','apellido','cuil','correo','crear_usuario')
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'cuil': forms.TextInput(attrs={'class': 'form-control'}),
            'correo': forms.EmailInput(attrs={'class': 'form-control'}),
            'crear_usuario': forms.CheckboxInput(attrs={'class': 'form-control'}),
        }


class AlumnoForm(forms.ModelForm):
    class Meta:
        model = Alumno
        fields = ('nombre', 'apellido', 'dni','matricula','correo',)
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'correo': forms.EmailInput(attrs={'class': 'form-control'}),
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
