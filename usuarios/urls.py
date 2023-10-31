from django.urls import path
from usuarios.views import index_admin

app_name = 'usuarios'
urlpatterns = [

    path('', index_admin, name='index_admin'),
]