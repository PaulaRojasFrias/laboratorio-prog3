from django.urls import path
from .views import registro_docente,  registro_alumno, registro_asesor

app_name = 'persona'
urlpatterns = [
    path('regDocente/', registro_docente, name='registro_docente'),
    path('regAlumno/', registro_alumno, name='registro_alumno'),
    path('regAsesor/', registro_asesor, name='registro_asesor'),
]