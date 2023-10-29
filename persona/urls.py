from django.urls import path
from .views import registro_docente,  registro_alumno, registro_asesor, lista_docente, detalle_docente, edit_docente, delete_docente, lista_alumno, detalle_alumno, edit_alumno, delete_alumno, lista_asesor, detalle_asesor, edit_asesor, delete_asesor

app_name = 'persona'
urlpatterns = [
    path('regDocente/', registro_docente, name='registro_docente'),
    path('listaDocente/', lista_docente, name='lista_docente'),
    path('detalleDocente/<int:pk>/', detalle_docente, name='detalle_docente'),
    path('editDocente/<int:pk>', edit_docente, name='edit_docente'),
    path('deleteDocente/', delete_docente, name='delete_docente'),


    path('regAlumno/', registro_alumno, name='registro_alumno'),
    path('listaAlumno/', lista_alumno, name='lista_alumno'),
    path('detalleAlumno/<int:pk>/', detalle_alumno, name='detalle_alumno'),
    path('editAlumno/<int:pk>', edit_alumno, name='edit_alumno'),
    path('deleteAlumno/', delete_alumno, name='delete_alumno'),


    path('regAsesor/', registro_asesor, name='registro_asesor'),
    path('listaAsesor/', lista_asesor, name='lista_asesor'),
    path('detalleAsesor/<int:pk>/', detalle_asesor, name='detalle_asesor'),
    path('editAsesor/<int:pk>', edit_asesor, name='edit_asesor'),
    path('deleteAsesor/', delete_asesor, name='delete_asesor'),

]