from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import AlumnoForm, CursoForm, NotaAlumnoPorCursoForm
from .models import Alumno, Curso, NotaAlumnoPorCurso

def crear_alumno(request):
    if request.method == "POST":
        form = AlumnoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_alumnos')
    else:
        form = AlumnoForm()
    return render(request, 'core/crear_alumno.html', {'form': form})

def crear_curso(request):
    if request.method == "POST":
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_cursos')
    else:
        form = CursoForm()
    return render(request, 'core/crear_curso.html', {'form': form})

def crear_nota(request):
    if request.method == "POST":
        form = NotaAlumnoPorCursoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_notas')
    else:
        form = NotaAlumnoPorCursoForm()
    return render(request, 'core/crear_nota.html', {'form': form})

def lista_alumnos(request):
    alumnos = Alumno.objects.all()
    return render(request, 'core/lista_alumnos.html', {'alumnos': alumnos})

def lista_cursos(request):
    cursos = Curso.objects.all()
    return render(request, 'core/lista_cursos.html', {'cursos': cursos})

def lista_notas(request):
    notas = NotaAlumnoPorCurso.objects.select_related('alumno', 'curso')
    return render(request, 'core/lista_notas.html', {'notas': notas})

def home(request):
    return render(request, 'core/home.html')

def crear_alumno(request):
    if request.method == 'POST':
        form = AlumnoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_alumnos')
    else:
        form = AlumnoForm()
    return render(request, 'core/crear_alumno.html', {'form': form})

def crear_nota(request):
    if request.method == 'POST':
        form = NotaAlumnoPorCursoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_notas')
    else:
        form = NotaAlumnoPorCursoForm()
    return render(request, 'core/crear_nota.html', {'form': form})