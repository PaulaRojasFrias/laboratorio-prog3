from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.contrib import messages
from comisiones.forms import ComisionForm
from .models import Comision

#COMISION DE SEGUIMIENTO DE TRABAJO FINAL
def cstf_lista(request): 
    comisiones = Comision.objects.all()
    return render(request, 'comisiones/lista.html', {'comisiones': comisiones})

def cstf_detalle(request, pk):
    comision = get_object_or_404(Comision, pk=pk)
    return render(request, 'comisiones/detalle.html', {'comision': comision})

def cstf_create(request):
    nueva_cstf = None
    if request.method == 'POST':
        comision_form = ComisionForm(request.POST, request.FILES)
        if comision_form.is_valid():
            #se guardan los datos que provienen del formulario en la B.D
            nueva_cstf = comision_form.save(commit=True)
            messages.success(request, 'Se ha agrgado correctamente la Comision {}' .format(nueva_cstf))
            return redirect(reverse('comisiones:cstf_detalle', args={nueva_cstf.id}))
    else:
        comision_form = ComisionForm()

    return render(request, 'comisiones/comision_form.html', {'form': comision_form})

def cstf_edit(request, pk):
    comision = get_object_or_404(Comision, pk=pk)
    if request.method == 'POST':
        comision_form = ComisionForm(request.POST, request.FILES, instance=comision)
        if comision_form.is_valid():
            comision_form.save()
            messages.success(request, 'Se ha actualizado correctamente la Comision')
            return redirect(reverse('comisiones:cstf_detalle', args=[comision.id]))
    else:
        comision_form = ComisionForm(instance=comision)

    return render(request, 'comisiones/comision_edit.html', {'form': comision_form})

def cstf_delete(request):
    if request.method == 'POST':
        if 'id_comision' in request.POST:
            comision = get_object_or_404(Comision, pk=request.POST['id_comision'])
            resolucionComision = comision.nroResolucionComision
            comision.delete()
            messages.success(request, 'Se ha eliminado existosamente la comision con nro. de resolucion {}' .format(resolucionComision))
        else:
            messages.error(request, 'Debe indicar que Comision desea eliminar')
    return redirect(reverse('comisiones:cstf_lista'))
#TRIBUNAL EVALUADOR