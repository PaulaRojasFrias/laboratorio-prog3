from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.contrib import messages
from comisiones.forms import ComisionForm, IntegranteComisionForm, TribunalForm
from .models import Comision, IntegrantesComision, TribunalEvaluador


#<<<<<<<<<<<<<<<<<<<<<<<<< COMISION DE SEGUIMIENTO DE TRABAJO FINAL >>>>>>>>>>>>>>>>>>>>>>
def cstf_lista(request): 
    comisiones = Comision.objects.all()
    return render(request, 'comisiones/comisiones_lista.html', {'comisiones': comisiones})

def cstf_detalle(request, pk):
    comision = get_object_or_404(Comision, pk=pk)
    integrantes = IntegrantesComision.objects.filter(comision=comision)
    return render(request, 'comisiones/comisiones_detalle.html', {'comision': comision, 'integrantes': integrantes})

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



#<<<<<<<<<<<<<<<<<<<<<<<<< Integrate de la Comision >>>>>>>>>>>>>>>>>>>>>>
def integranteComision_create(request):
    nuevoIntegrante = None
    if(request.method == 'POST'):
        integranteForm = IntegranteComisionForm(request.POST, request.FILES)
        if integranteForm.is_valid():
            nuevoIntegrante = integranteForm.save(commit=True)
            messages.success(request, 'Se ha agrgado correctamente el nuevo integrante')
            return redirect(reverse('comisiones:integranteComision_detalle', args=[nuevoIntegrante.id]))
    else:
        integranteForm = IntegranteComisionForm()

    return render(request, 'comisiones/integranteComision_form.html', {'form': integranteForm})

def integranteComision_detalle(request, pk):
    integrante = get_object_or_404(IntegrantesComision, pk=pk)
    return render(request, 'comisiones/integranteComision_detalle.html', {'integrante': integrante})

def integranteComision_edit(request, pk):
    integrante = get_object_or_404(IntegrantesComision, pk=pk)
    if request.method == 'POST':
        integrante_form = IntegranteComisionForm(request.POST, request.FILES, instance=integrante)
        if integrante_form.is_valid():
            integrante_form.save()
            messages.success(request, 'Se ha actualizado correctamente el integrante')
            return redirect(reverse('comisiones:integranteComision_detalle', args=[integrante.id]))
    else:
        integrante_form = IntegranteComisionForm(instance=integrante)

    return render(request, 'comisiones/integranteComision_edit.html', {'form': integrante_form})

def integranteComision_delete(request):
    if request.method == 'POST':
        if 'id_integrante' in request.POST:
            integrante = get_object_or_404(IntegrantesComision, pk=request.POST['id_integrante'])
            docente = integrante.docente
            integrante.delete()
            messages.success(request, 'Se ha eliminado existosamente el integrante  {}' .format(docente))
        else:
            messages.error(request, 'Debe indicar que Integrante desea eliminar')
    return redirect(reverse('comisiones:cstf_lista'))


#<<<<<<<<<<<<<<<<<<<<<<<<< TRIBUNAL EVALUADOR >>>>>>>>>>>>>>>>>>>>>>
def te_lista(request): 
    tribunales = TribunalEvaluador.objects.all()
    return render(request, 'comisiones/tribunal_lista.html', {'tribunales': tribunales})

def te_detalle(request, pk):
    tribunal = get_object_or_404(TribunalEvaluador, pk=pk)
    return render(request, 'comisiones/tribunal_detalle.html', {'tribunal': tribunal})

def te_create(request):
    nueva_te = None
    if request.method == 'POST':
        tribunal_form = TribunalForm(request.POST, request.FILES)
        if tribunal_form.is_valid():
            #se guardan los datos que provienen del formulario en la B.D
            nueva_te = tribunal_form.save(commit=True)
            messages.success(request, 'Se ha agrgado correctamente el Tribunal {}' .format(nueva_te))
            return redirect(reverse('comisiones:te_detalle', args={nueva_te.id}))
    else:
        tribunal_form = TribunalForm()

    return render(request, 'comisiones/tribunal_form.html', {'form': tribunal_form})


def te_edit(request, pk):
    tribunal = get_object_or_404(TribunalEvaluador, pk=pk)
    if request.method == 'POST':
        tribunal_form = TribunalForm(request.POST, request.FILES, instance=tribunal)
        if tribunal_form.is_valid():
            tribunal_form.save()
            messages.success(request, 'Se ha actualizado correctamente el Tribunal')
            return redirect(reverse('comisiones:te_detalle', args=[tribunal.id]))
    else:
        tribunal_form = TribunalForm(instance=tribunal)
    return render(request, 'comisiones/tribunal_edit.html', {'form': tribunal_form})

def te_delete(request):
    if request.method == 'POST':
        if 'id_tribunal' in request.POST:
            tribunal = get_object_or_404(TribunalEvaluador, pk=request.POST['id_tribunal'])
            disposicionTribunal = tribunal.nroDisposicionTribunal
            tribunal.delete()
            messages.success(request, 'Se ha eliminado existosamente el tribunal con el nro. de disposicion {}' .format(disposicionTribunal))
        else:
            messages.error(request, 'Debe indicar que Tribunal desea eliminar')
    return redirect(reverse('comisiones:te_lista'))

