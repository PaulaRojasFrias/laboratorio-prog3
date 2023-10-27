from django.urls import path

from comisiones.views import cstf_create, cstf_delete, cstf_detalle, cstf_edit, cstf_lista

app_name = 'comisiones'

urlpatterns = [
    #Comisiones views
    path('', cstf_lista, name='cstf_lista'), #no recibe argumentos
    path('<int:pk>/', cstf_detalle, name='cstf_detalle'), #recibe un argumento pk
    path('create/', cstf_create, name='cstf_create'),
    path('edit/<int:pk>', cstf_edit, name='cstf_edit'),
    path('delete/', cstf_delete, name='cstf_delete'),
]