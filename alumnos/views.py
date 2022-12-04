from django.shortcuts import render, redirect
from .models import Alumnos
from .forms import AlumnoForm


# Create your views here.

def home(request):
    return render(request,'home.html')


def session(request):
    formulario = AlumnoForm(request.POST or None)
    if(formulario.is_valid()):
        formulario.save()
        return redirect('mostrar')
    return render(request,'session.html', {'formulario': formulario})

def mostrar(request):
    alumnos = Alumnos.objects.all()
    return render(request,'mostrar.html', {'alumnos':alumnos})    

def eliminar(request,id):
    alumnos = Alumnos.objects.get(id_alumno=id)
    alumnos.delete()
    return redirect('mostrar')