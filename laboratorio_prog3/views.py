from django.http import HttpResponse
from django.shortcuts import render
def home(request):
  return render(request,'home.html')

def regAlumno(request):
  return render(request,'regAlumno.html')

def regCSTF(request):
  return render(request,'regCSTF.html')

def regTribunal(request):
  return render(request,'regTribunal.html')