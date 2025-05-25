from django.shortcuts import render, redirect
from .forms import AlumnoForm, CursoForm, NotaForm
from .models import Alumno, Curso, NotaAlumnoCurso

def menu_principal(request):
    return render(request, 'alumnos/menu_principal.html')

def crear_alumno(request):
    if request.method == 'POST':
        form = AlumnoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_alumnos')
    else:
        form = AlumnoForm()
    return render(request, 'alumnos/crear_alumno.html', {'form': form})

def lista_alumnos(request):
    alumnos = Alumno.objects.all()
    return render(request, 'alumnos/lista_alumnos.html', {'alumnos': alumnos})

def crear_curso(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_cursos')
    else:
        form = CursoForm()
    return render(request, 'alumnos/crear_curso.html', {'form': form})

def lista_cursos(request):
    cursos = Curso.objects.all()
    return render(request, 'alumnos/lista_cursos.html', {'cursos': cursos})

def crear_nota(request):
    if request.method == 'POST':
        form = NotaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_notas')
    else:
        form = NotaForm()
    return render(request, 'alumnos/crear_nota.html', {'form': form})

def lista_notas(request):
    notas = NotaAlumnoCurso.objects.all()
    return render(request, 'alumnos/lista_notas.html', {'notas': notas})