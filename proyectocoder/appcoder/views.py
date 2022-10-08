
import email
from http.client import HTTPResponse
from django.shortcuts import render

from django.http import HttpResponse
from appcoder.models import Estudiante

def mostrar_inicio(request):
    return HttpResponse("Hola mundo")


def mostrar_inicio(request):
    estudiante = Estudiante(nombre="Gaston", apellido="Morales", email="gaston@coder.com")
    contexto = {"estudiante_1": estudiante}
    return render(request, "appcoder/inicio.html", contexto)

def mostrar_cursos(request):
    return render(request, "appcoder/cursos.html")

def mostrar_entregables(request):
    return render(request, "appcoder/mostrar_entregables.html")

def mostrar_estudiantes(request):
    return render(request, "appcoder/mostrar_estudiantes.html")

def mostrar_profesores(request):
    return render(request, "appcoder/mostrar_profesores.html")

