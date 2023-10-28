from django.urls import path

from comisiones.views import cstf_create, cstf_delete, cstf_detalle, cstf_edit, cstf_lista, te_create, te_delete, te_detalle, te_edit, te_lista

app_name = 'comisiones'

urlpatterns = [
    #Comisiones views
    path('comision/', cstf_lista, name='cstf_lista'), 
    path('comision/<int:pk>/', cstf_detalle, name='cstf_detalle'), 
    path('comision/create/', cstf_create, name='cstf_create'),
    path('comision/<int:pk>', cstf_edit, name='cstf_edit'),
    path('comision/delete/', cstf_delete, name='cstf_delete'),
    
    path('tribunal', te_lista, name='te_lista'), #no recibe argumentos
    path('tribunal/<int:pk>/', te_detalle, name='te_detalle'), 
    path('tribunal/create/', te_create, name='te_create'),
    path('tribunal/<int:pk>', te_edit, name='te_edit'),
    path('tribunal/delete/', te_delete, name='te_delete'),
]