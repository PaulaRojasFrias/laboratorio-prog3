from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib import messages
from .forms import EvaluacionPTF_CSTFForm, EvaluacionPTF_TEForm, EvaluacionITFForm
from .models import EvaluacionPTF_CSTF, EvaluacionPTF_TE, EvaluacionITF
# Create your views here.

# Vistas para EvaluacionPTF_CSTF
def evaluacion_ptf_cstf_lista(request):
    evaluaciones = EvaluacionPTF_CSTF.objects.all()
    return render(request, 'dictamenes/templates/evaluacion_ptf_cstf_form.html', {'evaluaciones': evaluaciones})
def evaluacion_ptf_cstf_detalle(request, pk):
    evaluacion = get_object_or_404(EvaluacionPTF_CSTF, pk=pk)
    return render(request, 'dictamenes/templates/evaluacion_ptf_cstf_detalle.html', {'evaluacion': evaluacion})
def evaluacion_ptf_cstf_create(request):
    nueva_evaluacion = None
    if request.method == 'POST':
        evaluacion_form = EvaluacionPTF_CSTFForm(request.POST, request.FILES)
        if evaluacion_form.is_valid():
            nueva_evaluacion = evaluacion_form.save()

            return redirect('dictamenes:evaluacion_ptf_cstf_detalle', pk=nueva_evaluacion.pk)
    else:
        evaluacion_form = EvaluacionPTF_CSTFForm()
    return render(request, 'dictamenes/templates/evaluacion_ptf_cstf_form.html', {'form': evaluacion_form})
def evaluacion_ptf_cstf_edit(request, pk):
    evaluacion = get_object_or_404(EvaluacionPTF_CSTF, pk=pk)
    if request.method == 'POST':
        evaluacion_form = EvaluacionPTF_CSTFForm(request.POST, request.FILES, instance=evaluacion)
        if evaluacion_form.is_valid():
            evaluacion_form.save()
            return redirect('dictamenes:evaluacion_ptf_cstf_detalle', pk=evaluacion.pk)
    else:
        evaluacion_form = EvaluacionPTF_CSTFForm(instance=evaluacion)
    return render(request, 'dictamenes/templates/evaluacion_ptf_cstf_form.html', {'form': evaluacion_form})
def evaluacion_ptf_cstf_delete(request, pk):
    evaluacion = get_object_or_404(EvaluacionPTF_CSTF, pk=pk)
    if request.method == 'POST':
        evaluacion.delete()
        messages.success(request, f'Se ha eliminado existosamente la evaluación PTF CSTF con ID: {pk}')
        return redirect('dictamenes:evaluacion_ptf_cstf_lista')
    return render(request, 'dictamenes/templates/evaluacion_ptf_cstf_confirm_delete.html', {'evaluacion': evaluacion})





# Vistas para EvaluacionPTF_TE
def evaluacion_ptf_te_lista(request):
    evaluaciones = EvaluacionPTF_TE.objects.all()
    return render(request, 'dictamenes/templates/evaluacion_ptf_te_form.html', {'evaluaciones': evaluaciones})
def evaluacion_ptf_te_detalle(request, pk):
    evaluacion = get_object_or_404(EvaluacionPTF_TE, pk=pk)
    return render(request, 'dictamenes/templates/evaluacion_ptf_te_detalle.html', {'evaluacion': evaluacion})
def evaluacion_ptf_te_create(request):
    nueva_evaluacion = None
    if request.method == 'POST':
        evaluacion_form = EvaluacionPTF_TEForm(request.POST, request.FILES)
        if evaluacion_form.is_valid():
            nueva_evaluacion = evaluacion_form.save()
            # Realiza cualquier otra lógica necesaria aquí
            return redirect('dictamenes:evaluacion_ptf_te_detalle', pk=nueva_evaluacion.pk)
    else:
        evaluacion_form = EvaluacionPTF_TEForm()
    return render(request, 'dictamenes/templates/evaluacion_ptf_te_form.html', {'form': evaluacion_form})
def evaluacion_ptf_te_edit(request, pk):
    evaluacion = get_object_or_404(EvaluacionPTF_TE, pk=pk)
    if request.method == 'POST':
        evaluacion_form = EvaluacionPTF_TEForm(request.POST, request.FILES, instance=evaluacion)
        if evaluacion_form.is_valid():
            evaluacion_form.save()
            # Realiza cualquier otra lógica necesaria aquí
            return redirect('dictamenes:evaluacion_ptf_te_detalle', pk=evaluacion.pk)
    else:
        evaluacion_form = EvaluacionPTF_TEForm(instance=evaluacion)
    return render(request, 'dictamenes/templates/evaluacion_ptf_te_form.html', {'form': evaluacion_form})
def evaluacion_te_delete(request, pk):
    evaluacion = get_object_or_404(EvaluacionPTF_TE, pk=pk)
    if request.method == 'POST':
        evaluacion.delete()
        messages.success(request, f'Se ha eliminado existosamente la evaluación TE con ID: {pk}')
        return redirect('dictamenes:evaluacion_ptf_te_lista')
    return render(request, 'dictamenes/templates/evaluacion_te_confirm_delete.html', {'evaluacion': evaluacion})


# Vistas para EvaluacionITF
def evaluacion_itf_lista(request):
    evaluaciones = EvaluacionITF.objects.all()
    return render(request, 'dictamenes/templates/evaluacion_itf_form.html', {'evaluaciones': evaluaciones})
def evaluacion_itf_detalle(request, pk):
    evaluacion = get_object_or_404(EvaluacionITF, pk=pk)
    return render(request, 'dictamenes/templates/evaluacion_itf_detalle.html', {'evaluacion': evaluacion})
def evaluacion_itf_create(request):
    nueva_evaluacion = None
    if request.method == 'POST':
        evaluacion_form = EvaluacionITFForm(request.POST, request.FILES)
        if evaluacion_form.is_valid():
            nueva_evaluacion = evaluacion_form.save()
            # Realiza cualquier otra lógica necesaria aquí
            return redirect('dictamenes:evaluacion_itf_detalle', pk=nueva_evaluacion.pk)
    else:
        evaluacion_form = EvaluacionITFForm()
    return render(request, 'dictamenes/templates/evaluacion_itf_form.html', {'form': evaluacion_form})
def evaluacion_itf_edit(request, pk):
    evaluacion = get_object_or_404(EvaluacionITF, pk=pk)
    if request.method == 'POST':
        evaluacion_form = EvaluacionITFForm(request.POST, request.FILES, instance=evaluacion)
        if evaluacion_form.is_valid():
            evaluacion_form.save()
            # Realiza cualquier otra lógica necesaria aquí
            return redirect('dictamenes:evaluacion_itf_detalle', pk=evaluacion.pk)
    else:
        evaluacion_form = EvaluacionITFForm(instance=evaluacion)
    return render(request, 'dictamenes/templates/evaluacion_itf_form.html', {'form': evaluacion_form})
def evaluacion_itf_delete(request, pk):
    evaluacion = get_object_or_404(EvaluacionITF, pk=pk)
    if request.method == 'POST':
        evaluacion.delete()
        messages.success(request, f'Se ha eliminado existosamente la evaluación ITF con ID: {pk}')
        return redirect('dictamenes:evaluacion_itf_lista')
    return render(request, 'dictamenes/templates/evaluacion_itf_confirm_delete.html', {'evaluacion': evaluacion})