from django.urls import path
from usuarios.views import index_admin, login_view, logout_view

app_name = 'usuarios'
urlpatterns = [

    path('', index_admin, name='index_admin'),
    path('login', login_view, name='login_view'),
    path('logout', logout_view, name='logout_view'),
]