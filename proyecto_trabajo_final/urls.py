from django.urls import path

from proyecto_trabajo_final.views import integranteProyecto_create, integranteProyecto_delete, integranteProyecto_detalle, integranteProyecto_edit, proyecto_create, proyecto_delete, proyecto_detalle, proyecto_edit, proyecto_lista

app_name = 'proyecto_trabajo_final'
urlpatterns = [
    path('proyecto/', proyecto_lista, name='proyecto_lista'),
    path('proyecto/<int:pk>/', proyecto_detalle, name='proyecto_detalle'),
    path('proyecto/create/', proyecto_create, name='proyecto_create'),
    path('proyecto/edit/<int:pk>/', proyecto_edit, name='proyecto_edit'),
    path('proyecto/delete/', proyecto_delete, name='proyecto_delete'),

    
    path('integrante/create', integranteProyecto_create, name='integranteProyecto_create'),
    path('integrante/<int:pk>/', integranteProyecto_detalle, name='integranteProyecto_detalle'),
    path('integrante/edit/<int:pk>/', integranteProyecto_edit, name='integranteProyecto_edit'),
    path('integrante/delete/', integranteProyecto_delete, name='integranteProyecto_delete'),
]
