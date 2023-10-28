from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.contrib import messages
from proyecto_trabajo_final.forms import IntegranteProyectoForm, ProyectoForm

from proyecto_trabajo_final.models import PTF_Integrantes, ProyectoFinal

def proyecto_lista(request):
    proyectos = ProyectoFinal.objects.all()
    return render(request, 'proyecto_trabajo_final/proyecto_lista.html', {'proyectos': proyectos})

def proyecto_detalle(request, pk):
    proyecto = get_object_or_404(ProyectoFinal, pk=pk)
    integrantes = PTF_Integrantes.objects.filter(proyectoFinal=proyecto)
    return render(request, 'proyecto_trabajo_final/proyecto_detalle.html', {'proyecto': proyecto, 'integrantes':integrantes})

def proyecto_create(request):
    nuevo_proyecto = None
    if request.method == 'POST':
        proyecto_form = ProyectoForm(request.POST, request.FILES)
        if proyecto_form.is_valid():
            #se guardan los datos que provienen del formulario en la B.D
            nuevo_proyecto = proyecto_form.save(commit=True)
            messages.success(request, 'Se ha agrgado correctamente el proyecto {}' .format(nuevo_proyecto))
            return redirect(reverse('proyecto_trabajo_final:proyecto_detalle', args={nuevo_proyecto.id}))
    else:
        proyecto_form = ProyectoForm()

    return render(request, 'proyecto_trabajo_final/proyecto_form.html', {'form': proyecto_form})

def proyecto_edit(request, pk):
    proyecto = get_object_or_404(ProyectoFinal, pk=pk)
    if request.method == 'POST':
        proyecto_form = ProyectoForm(request.POST, request.FILES, instance=proyecto)
        if proyecto_form.is_valid():
            proyecto_form.save()
            messages.success(request, 'Se ha actualizado correctamente el proyecto')
            return redirect(reverse('proyecto_trabajo_final:proyecto_detalle', args=[proyecto.id]))
    else:
        proyecto_form = ProyectoForm(instance=proyecto)

    return render(request, 'proyecto_trabajo_final/proyecto_edit.html', {'form': proyecto_form})

def proyecto_delete(request):
    if request.method == 'POST':
        if 'id_proyecto' in request.POST:
            proyecto = get_object_or_404(ProyectoFinal, pk=request.POST['id_proyecto'])
            titulo = proyecto.titulo
            proyecto.delete()
            messages.success(request, 'Se ha eliminado existosamente el proyecto {}' .format(titulo))
        else:
            messages.error(request, 'Debe indicar que proyecto desea eliminar')
    return redirect(reverse('proyecto_trabajo_final:proyecto_lista'))


def integranteProyecto_detalle(request, pk):
    integrante = get_object_or_404(PTF_Integrantes, pk=pk)
    return render(request, 'proyecto_trabajo_final/integranteProyecto_detalle.html', {'integrante': integrante})


def integranteProyecto_create(request):
    nuevoIntegrante = None
    if(request.method == 'POST'):
        integranteForm = IntegranteProyectoForm(request.POST, request.FILES)
        if integranteForm.is_valid():
            nuevoIntegrante = integranteForm.save(commit=True)
            messages.success(request, 'Se ha agrgado correctamente el nuevo integrante')
            return redirect(reverse('proyecto_trabajo_final:integranteProyecto_detalle', args=[nuevoIntegrante.id]))
    else:
        integranteForm = IntegranteProyectoForm()

    return render(request, 'proyecto_trabajo_final/integranteProyecto_form.html', {'form': integranteForm})


def integranteProyecto_delete(request):
    if request.method == 'POST':
        if 'id_integrante' in request.POST:
            integrante = get_object_or_404(PTF_Integrantes, pk=request.POST['id_integrante'])
            alumno = integrante.alumnos
            integrante.delete()
            messages.success(request, 'Se ha eliminado existosamente el integrante  {}' .format(alumno))
        else:
            messages.error(request, 'Debe indicar que Integrante desea eliminar')
    return redirect(reverse('proyecto_trabajo_final:proyecto_lista'))

def integranteProyecto_edit(request, pk):
    integrante = get_object_or_404(PTF_Integrantes, pk=pk)
    if request.method == 'POST':
        integrante_form = IntegranteProyectoForm(request.POST, request.FILES, instance=integrante)
        if integrante_form.is_valid():
            integrante_form.save()
            messages.success(request, 'Se ha actualizado correctamente el integrante')
            return redirect(reverse('proyecto_trabajo_final:integranteProyecto_detalle', args=[integrante.id]))
    else:
        integrante_form = IntegranteProyectoForm(instance=integrante)

    return render(request, 'proyecto_trabajo_final/integranteProyecto_edit.html', {'form': integrante_form})
