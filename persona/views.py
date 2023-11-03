from django.db import IntegrityError
from django.shortcuts import render, get_object_or_404, redirect
from .models import Docente, Alumno, Asesor
from .forms import DocenteForm, AlumnoForm, AsesorForm
from django.urls import reverse
from django.db.models import Q
from django.contrib import messages

# Create your views here.
#<<<<<<<<<<<<<<<<<<<<<<< DOCENTE >>>>>>>>>>>>>>>>>>>>>>
def registro_docente(request):
    form = DocenteForm()

    if request.method == 'POST':
        form = DocenteForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form': form}

    return render(request, 'persona/regDocente.html', context)


def lista_docente(request):
    docentes = Docente.objects.all()
    return render(request, 'persona/listaDocente.html', {'docentes': docentes})

def detalle_docente(request, pk):
    docente = get_object_or_404(Docente, pk=pk)
    return render(request, 'persona/detalleDocente.html', {'docente': docente})

def edit_docente(request, pk):
    docente = get_object_or_404(Docente, pk=pk)
    if request.method == 'POST':
        docente_form = DocenteForm(request.POST, request.FILES, instance=docente)
        if docente_form.is_valid():
            docente_form.save()
            messages.success(request, 'Se ha actualizado correctamente el docente')
            return redirect(reverse('persona:detalle_docente', args=[docente.id]))
    else:
        docente_form = DocenteForm(instance=docente)

    return render(request, 'persona/editDocente.html', {'form': docente_form})


def delete_docente(request):
    if request.method == 'POST':
        if 'id_docente' in request.POST:
            docente = get_object_or_404(Docente, pk=request.POST['id_docente'])
            docente.delete()
            messages.success(request, 'Se ha eliminado existosamente el docente  {}' )
        else:
            messages.error(request, 'Debe indicar que Docente desea eliminar')
    return redirect(reverse('persona:lista_docente'))



#<<<<<<<<<<<<<<<<<<<<<<< ALUMNO >>>>>>>>>>>>>>>>>>>>>>

def registro_alumno(request):
    nuevo_alumno= None
    if request.method == 'POST':
        form = AlumnoForm(request.POST)
        if form.is_valid():
            try:
                nuevo_alumno = form.save(commit=True)
                messages.success(request, 'El alumno ha sido registrado exitosamente.')
                return redirect(reverse('persona:detalle_alumno', args={nuevo_alumno.id}))
            except IntegrityError:
                messages.error(request, 'Ya existe un alumno con ese DNI o matricula.')
                return render(request,'persona/regAlumno.html', { 'form': form })
   
    else:
        form = AlumnoForm()

    return render(request, 'persona/regAlumno.html', {'form': form})


def lista_alumno(request):
    busqueda = request.GET.get("buscar")
    alumnos = Alumno.objects.all()
    if busqueda:
        alumnos = Alumno.objects.filter(
            Q(dni__icontains = busqueda) |
            Q(matricula__icontains = busqueda) |
            Q(correo__icontains = busqueda) |
            Q(nombre__icontains = busqueda) |
            Q(apellido__icontains = busqueda)
        ).distinct()
    return render(request, 'persona/listaAlumno.html', {'alumnos': alumnos})


def detalle_alumno(request, pk):
    alumno = get_object_or_404(Alumno, pk=pk)
    return render(request, 'persona/detalleAlumno.html', {'alumno': alumno})


def edit_alumno(request, pk):
    alumno = get_object_or_404(Alumno, pk=pk)
    if request.method == 'POST':
        alumno_form = AlumnoForm(request.POST, request.FILES, instance=alumno)
        if alumno_form.is_valid():
            alumno_form.save()
            messages.success(request, 'Se ha actualizado correctamente el alumno')
            return redirect(reverse('persona:detalle_alumno', args=[alumno.id]))
    else:
        alumno_form = AlumnoForm(instance=alumno)

    return render(request, 'persona/editAlumno.html', {'form': alumno_form})



def delete_alumno(request):
    if request.method == 'POST':
        if 'id_alumno' in request.POST:
            alumno = get_object_or_404(Alumno, pk=request.POST['id_alumno'])
            alumno.delete()
            messages.success(request, 'Se ha eliminado existosamente el alumno ')
        else:
            messages.error(request, 'Debe indicar que Alumno desea eliminar')
    return redirect(reverse('persona:lista_alumno'))



#<<<<<<<<<<<<<<<<<<<<<<< ASESOR >>>>>>>>>>>>>>>>>>>>>>

def registro_asesor(request):
    form = AsesorForm()

    if request.method == 'POST':
        form = AsesorForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form': form}

    return render(request, 'persona/regAsesor.html', context)


def lista_asesor(request):
    asesores = Asesor.objects.all()
    return render(request, 'persona/listaAsesor.html', {'asesores': asesores})


def detalle_asesor(request, pk):
    asesor = get_object_or_404(Asesor, pk=pk)
    return render(request, 'persona/detalleAsesor.html', {'asesor': asesor})


def edit_asesor(request, pk):
    asesor = get_object_or_404(Asesor, pk=pk)
    if request.method == 'POST':
        asesor_form = AsesorForm(request.POST, request.FILES, instance=asesor)
        if asesor_form.is_valid():
            asesor_form.save()
            messages.success(request, 'Se ha actualizado correctamente el asesor')
            return redirect(reverse('persona:detalle_asesor', args=[asesor.id]))
    else:
        asesor_form = DocenteForm(instance=asesor)

    return render(request, 'persona/editAsesor.html', {'form': asesor_form})

def delete_asesor(request):
    if request.method == 'POST':
        if 'id_asesor' in request.POST:
            asesor = get_object_or_404(Asesor, pk=request.POST['id_asesor'])
            asesor.delete()
            messages.success(request, 'Se ha eliminado existosamente el asesor  {}' )
        else:
            messages.error(request, 'Debe indicar que asesor desea eliminar')
    return redirect(reverse('persona:lista_asesor'))
