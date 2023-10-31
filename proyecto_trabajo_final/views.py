from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.contrib import messages
from django.views.generic import ListView
from datetime import datetime
from comisiones.models import TribunalEvaluador
from proyecto_trabajo_final.forms import AsesorPTFForm, InformeFinalForm, IntegranteProyectoForm, MovimientoForm, \
    ProyectoForm, TutorForm, Informe1, Informe2

from proyecto_trabajo_final.models import AsesorPTF, InformeTF, Movimientos, PTF_Integrantes, ProyectoFinal, TutoresPTF

#<<<<<<<<<<<<<<<<<<<<<<<<< PROYECTO TRABAJO FINAL >>>>>>>>>>>>>>>>>>>>>>
def proyecto_lista(request):
    proyectos = ProyectoFinal.objects.all()
    return render(request, 'proyecto_trabajo_final/proyecto_lista.html', {'proyectos': proyectos})

def proyecto_detalle(request, pk):
    proyecto = get_object_or_404(ProyectoFinal, pk=pk)
    integrantes = PTF_Integrantes.objects.filter(proyectoFinal=proyecto)
    tutores = TutoresPTF.objects.filter(proyecto=proyecto)
    asesores = AsesorPTF.objects.filter(proyecto=proyecto)
    movimientos = Movimientos.objects.filter(proyecto=proyecto)
    informe = InformeTF.objects.filter(proyectoTF=proyecto)
    return render(request, 'proyecto_trabajo_final/proyecto_detalle.html', {'proyecto': proyecto, 'integrantes':integrantes, 'tutores': tutores, 'asesores': asesores, 'movimientos': movimientos, 'informes': informe})

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



#<<<<<<<<<<<<<<<<<<<<<<<<< ALUMNOS QUE CONFORMAN LOS PROYECTOS  >>>>>>>>>>>>>>>>>>>>>>

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


#<<<<<<<<<<<<<<<<<<<<<<<<< TUTORES QUE CONFORMAN LOS PROYECTOS  >>>>>>>>>>>>>>>>>>>>>>
def tutorProyecto_create(request, pk):
    proyecto = get_object_or_404(ProyectoFinal, pk=pk)
    nuevoIntegrante = None
    if(request.method == 'POST'):
        integranteForm = TutorForm(request.POST, request.FILES)
        if integranteForm.is_valid():
            nuevoIntegrante = integranteForm.save(commit=True)
            messages.success(request, 'Se ha agrgado correctamente el nuevo tutor')
            return redirect(reverse('proyecto_trabajo_final:proyecto_detalle', args=[proyecto.id]))
    else:
        integranteForm = TutorForm()

    return render(request, 'proyecto_trabajo_final/tutorProyecto_form.html', {'form': integranteForm})

def tutorProyecto_delete(request, pk):
    proyecto = get_object_or_404(ProyectoFinal, pk=pk)
    if request.method == 'POST':
        if 'id_tutor' in request.POST:
            integrante = get_object_or_404(TutoresPTF, pk=request.POST['id_tutor'])
            docente = integrante.docente
            integrante.delete()
            messages.success(request, 'Se ha eliminado existosamente el tutor  {}' .format(docente))
        else:
            messages.error(request, 'Debe indicar que tutor desea eliminar')
    return redirect(reverse('proyecto_trabajo_final:proyecto_detalle', args=[proyecto.id]))

def tutorProyecto_edit(request, pk, pk2):
    integrante = get_object_or_404(TutoresPTF, pk=pk)
    proyecto = get_object_or_404(ProyectoFinal, pk=pk2)
    if request.method == 'POST':
        integrante_form = TutorForm(request.POST, request.FILES, instance=integrante)
        if integrante_form.is_valid():
            integrante_form.save()
            messages.success(request, 'Se ha actualizado correctamente el tutor')
            return redirect(reverse('proyecto_trabajo_final:proyecto_detalle', args=[proyecto.id]))
    else:
        integrante_form = TutorForm(instance=integrante)

    return render(request, 'proyecto_trabajo_final/tutorProyecto_edit.html', {'form': integrante_form})

#<<<<<<<<<<<<<<<<<<<<<<<<< ASESORES QUE CONFORMAN LOS PROYECTOS  >>>>>>>>>>>>>>>>>>>>>>
def asesorProyecto_create(request, pk):
    proyecto = get_object_or_404(ProyectoFinal, pk=pk)
    nuevoAsesor = None
    if(request.method == 'POST'):
        asesorForm = AsesorPTFForm(request.POST, request.FILES)
        if asesorForm.is_valid():
            nuevoAsesor = asesorForm.save(commit=True)
            messages.success(request, 'Se ha agrgado correctamente el nuevo asesor')
            return redirect(reverse('proyecto_trabajo_final:proyecto_detalle', args=[proyecto.id]))
    else:
        asesorForm = AsesorPTFForm()

    return render(request, 'proyecto_trabajo_final/asesorProyecto_form.html', {'form': asesorForm})

def asesorProyecto_delete(request, pk):
    proyecto = get_object_or_404(ProyectoFinal, pk=pk)
    if request.method == 'POST':
        if 'id_asesor' in request.POST:
            asesorPro = get_object_or_404(AsesorPTF, pk=request.POST['id_asesor'])
            asesor = asesorPro.asesor
            asesorPro.delete()
            messages.success(request, 'Se ha eliminado existosamente el tutor  {}' .format(asesor))
        else:
            messages.error(request, 'Debe indicar que tutor desea eliminar')
    return redirect(reverse('proyecto_trabajo_final:proyecto_detalle', args=[proyecto.id]))

def asesorProyecto_edit(request, pk, pk2):
    asesor = get_object_or_404(AsesorPTF, pk=pk)
    proyecto = get_object_or_404(ProyectoFinal, pk=pk2)
    if request.method == 'POST':
        asesor_form = AsesorPTFForm(request.POST, request.FILES, instance=asesor)
        if asesor_form.is_valid():
            asesor_form.save()
            messages.success(request, 'Se ha actualizado correctamente el asesor')
            return redirect(reverse('proyecto_trabajo_final:proyecto_detalle', args=[proyecto.id]))
    else:
        asesor_form = AsesorPTFForm(instance=asesor)

    return render(request, 'proyecto_trabajo_final/asesorProyecto_edit.html', {'form': asesor_form})


def movimientoProyecto_edit(request, pk, pk2):
    movimiento = get_object_or_404(Movimientos, pk=pk)
    proyecto = get_object_or_404(ProyectoFinal, pk=pk2)
    if request.method == 'POST':
        movimiento_form = MovimientoForm(request.POST, request.FILES, instance=movimiento)
        if movimiento_form.is_valid():
            movimiento_form.save()
            messages.success(request, 'Se ha actualizado correctamente el movimiento')
            return redirect(reverse('proyecto_trabajo_final:proyecto_detalle', args=[proyecto.id]))
    else:
        movimiento_form = MovimientoForm(instance=movimiento)

    return render(request, 'proyecto_trabajo_final/movimientoProyecto_edit.html', {'form': movimiento_form})


#<<<<<<<<<<<<<<<<<<<<<<<<< INFORME FINAL QUE CONFORMAN LOS PROYECTOS  >>>>>>>>>>>>>>>>>>>>>>
def informeProyecto_create(request, pk):
    proyecto = get_object_or_404(ProyectoFinal, pk=pk)
    if(request.method == 'POST'):
        informeForm = InformeFinalForm(request.POST, request.FILES)
        if informeForm.is_valid():
            informeForm.save(commit=True)
            messages.success(request, 'Se ha agrgado correctamente el nuevo informe')
            return redirect(reverse('proyecto_trabajo_final:proyecto_detalle', args=[proyecto.id]))
    else:
        informeForm = InformeFinalForm()

    return render(request, 'proyecto_trabajo_final/informeProyecto_form.html', {'form': informeForm})


def informeProyecto_delete(request, pk):
    proyecto = get_object_or_404(ProyectoFinal, pk=pk)
    if request.method == 'POST':
        if 'id_informe' in request.POST:
            informe = get_object_or_404(InformeTF, pk=request.POST['id_informe'])
            informe.delete()
            messages.success(request, 'Se ha eliminado existosamente el informe')
        else:
            messages.error(request, 'Debe indicar que informe desea eliminar')
    return redirect(reverse('proyecto_trabajo_final:proyecto_detalle', args=[proyecto.id]))

def informeProyecto_edit(request, pk, pk2):
    informe = get_object_or_404(InformeTF, pk=pk)
    proyecto = get_object_or_404(ProyectoFinal, pk=pk2)
    if request.method == 'POST':
        informe_form = InformeFinalForm(request.POST, request.FILES, instance=informe)
        if informe_form.is_valid():
            informe_form.save()
            messages.success(request, 'Se ha actualizado correctamente el informe')
            return redirect(reverse('proyecto_trabajo_final:proyecto_detalle', args=[proyecto.id]))
    else:
        informe_form = InformeFinalForm(instance=informe)

    return render(request, 'proyecto_trabajo_final/informeProyecto_edit.html', {'form': informe_form})




#<<<<<<<<<<<<<<<<<<<<<<<<< ESTADISTICAS >>>>>>>>>>>>>>>>>>>>>>

def estadisticas(request):
    return render(request, 'proyecto_trabajo_final/estadisticas.html')

class Informe1(ListView):
    model = Movimientos
    template_name = 'proyecto_trabajo_final/informe1.html'
    form_class = Informe1
    def get_queryset(self):
        queryset = super().get_queryset()
        estado = self.request.GET.get('estado')
        fecha_inicio = self.request.GET.get('fecha_inicio')
        fecha_fin = self.request.GET.get('fecha_fin')

        if estado:
            queryset = queryset.filter(estado=estado)

        if fecha_inicio and fecha_fin:
            fecha_inicio = datetime.strptime(fecha_inicio, '%Y-%m-%d')
            fecha_fin = datetime.strptime(fecha_fin, '%Y-%m-%d')
            queryset = queryset.filter(proyecto__fechaPresentacion__range=(fecha_inicio, fecha_fin))

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.form_class(self.request.GET)
        return context


class Informe2(ListView):
    model = TribunalEvaluador
    template_name = 'proyecto_trabajo_final/informe2.html'
    form_class = Informe2

    def get_queryset(self):
        queryset = super().get_queryset()
        nroDisposicionTribunal = self.request.GET.get('nroDisposicionTribunal')

        if nroDisposicionTribunal:
            queryset = queryset.filter(nroDisposicionTribunal=nroDisposicionTribunal)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.form_class(self.request.GET)
        return context