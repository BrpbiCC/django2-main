from django.shortcuts import render
from .models import Alumno, Genero
# Create your views here.

def index (request):
    alumnos= Alumno.objects.all()
    context={"alumnos": alumnos}
    return render (request, 'alumnos/index.html', context)

def lista (request):
    alumnos= Alumno.objects.raw('selecto * from alumnos_alumno')
    context={"alumnos": alumnos}
    return render (request, 'alumnos/lista.html', context)