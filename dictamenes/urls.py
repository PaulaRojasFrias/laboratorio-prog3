from django.urls import path
from dictamenes.views import evaluacion_te_delete,evaluacion_itf_delete,evaluacion_itf_detalle,evaluacion_itf_edit,evaluacion_itf_lista,evaluacion_ptf_te_edit,evaluacion_ptf_te_lista,evaluacion_ptf_cstf_edit,evaluacion_ptf_te_create,evaluacion_ptf_cstf_create,evaluacion_ptf_te_detalle,evaluacion_ptf_cstf_delete,evaluacion_ptf_cstf_detalle,evaluacion_ptf_cstf_lista,evaluacion_itf_create

app_name = 'dictamenes'

urlpatterns = [
    # URLs para EvaluacionPTF_CSTF
    path('evaluacion_ptf_cstf_lista/', views.evaluacion_ptf_cstf_lista, name='evaluacion_ptf_cstf_lista'),
    path('evaluacion_ptf_cstf_detalle/<int:pk>/', views.evaluacion_ptf_cstf_detalle, name='evaluacion_ptf_cstf_detalle'),
    path('evaluacion_ptf_cstf_create/', views.evaluacion_ptf_cstf_create, name='evaluacion_ptf_cstf_create'),
    path('evaluacion_ptf_cstf_edit/<int:pk>/', views.evaluacion_ptf_cstf_edit, name='evaluacion_ptf_cstf_edit'),
    path('evaluacion_ptf_cstf_delete/<int:pk>/', views.evaluacion_ptf_cstf_delete, name='evaluacion_ptf_cstf_delete'),

    # URLs para EvaluacionPTF_TE
    path('evaluacion_ptf_te_lista/', views.evaluacion_ptf_te_lista, name='evaluacion_ptf_te_lista'),
    path('evaluacion_ptf_te_detalle/<int:pk>/', views.evaluacion_ptf_te_detalle, name='evaluacion_ptf_te_detalle'),
    path('evaluacion_ptf_te_create/', views.evaluacion_ptf_te_create, name='evaluacion_ptf_te_create'),
    path('evaluacion_ptf_te_edit/<int:pk>/', views.evaluacion_ptf_te_edit, name='evaluacion_ptf_te_edit'),
    path('evaluacion_ptf_te_delete/<int:pk>/', views.evaluacion_ptf_te_delete, name='evaluacion_ptf_te_delete'),

    # URLs para EvaluacionITF
    path('evaluacion_itf_lista/', views.evaluacion_itf_lista, name='evaluacion_itf_lista'),
    path('evaluacion_itf_detalle/<int:pk>/', views.evaluacion_itf_detalle, name='evaluacion_itf_detalle'),
    path('evaluacion_itf_create/', views.evaluacion_itf_create, name='evaluacion_itf_create'),
    path('evaluacion_itf_edit/<int:pk>/', views.evaluacion_itf_edit, name='evaluacion_itf_edit'),
    path('evaluacion_itf_delete/<int:pk>/', views.evaluacion_itf_delete, name='evaluacion_itf_delete'),
]