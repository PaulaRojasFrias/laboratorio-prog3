from django.urls import path

from proyecto_trabajo_final.views import asesorProyecto_create, asesorProyecto_delete, asesorProyecto_edit, \
    informeProyecto_create, informeProyecto_delete, informeProyecto_edit, integranteProyecto_create, \
    integranteProyecto_delete, integranteProyecto_detalle, integranteProyecto_edit, movimientoProyecto_edit, \
    proyecto_create, proyecto_delete, proyecto_detalle, proyecto_edit, proyecto_lista, tutorProyecto_create, \
    tutorProyecto_delete, tutorProyecto_edit, Informe1, Informe2, estadisticas

app_name = 'proyecto_trabajo_final'
urlpatterns = [
    path('proyecto/', proyecto_lista, name='proyecto_lista'),
    path('proyecto/<int:pk>/', proyecto_detalle, name='proyecto_detalle'),
    path('proyecto/create/', proyecto_create, name='proyecto_create'),
    path('proyecto/edit/<int:pk>/', proyecto_edit, name='proyecto_edit'),
    path('proyecto/delete/', proyecto_delete, name='proyecto_delete'),

    path('proyecto/estadisticas', estadisticas, name='estadisticas'),
    path('proyecto/informen1', Informe1.as_view(), name='proyecto_informen1'),
    path('proyecto/informen2', Informe2.as_view(), name='proyecto_informen2'),

    
    path('integrante/create', integranteProyecto_create, name='integranteProyecto_create'),
    path('integrante/<int:pk>/', integranteProyecto_detalle, name='integranteProyecto_detalle'),
    path('integrante/edit/<int:pk>/', integranteProyecto_edit, name='integranteProyecto_edit'),
    path('integrante/delete/', integranteProyecto_delete, name='integranteProyecto_delete'),

    path('tutor/create/<int:pk>', tutorProyecto_create, name='tutorProyecto_create'),
    path('tutor/delete/<int:pk>', tutorProyecto_delete, name='tutorProyecto_delete'),
    path('tutor/edit/<int:pk>/<int:pk2>', tutorProyecto_edit, name='tutorProyecto_edit'),

    path('asesor/create/<int:pk>', asesorProyecto_create, name='asesorProyecto_create'),
    path('asesor/delete/<int:pk>', asesorProyecto_delete, name='asesorProyecto_delete'),
    path('asesor/edit/<int:pk>/<int:pk2>', asesorProyecto_edit, name='asesorProyecto_edit'),

    
    path('movimiento/edit/<int:pk>/<int:pk2>', movimientoProyecto_edit, name='movimientoProyecto_edit'),

    path('informe/create/<int:pk>', informeProyecto_create, name='informeProyecto_create'),
    path('informe/delete/<int:pk>', informeProyecto_delete, name='informeProyecto_delete'),
    path('informe/edit/<int:pk>/<int:pk2>', informeProyecto_edit, name='informeProyecto_edit'),


]
