from django.shortcuts import render, get_object_or_404
#from .models import Docente
from .forms import DocenteForm, AlumnoForm, AsesorForm

# Create your views here.
def registro_docente(request):
    form = DocenteForm()

    if request.method == 'POST':
        form = DocenteForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form': form}

    return render(request, 'persona/regDocente.html', context)

def registro_alumno(request):
    form = AlumnoForm()

    if request.method == 'POST':
        form = AlumnoForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form': form}

    return render(request, 'persona/regAlumno.html', context)

def registro_asesor(request):
    form = AsesorForm()

    if request.method == 'POST':
        form = AsesorForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form': form}

    return render(request, 'persona/regAsesor.html', context)