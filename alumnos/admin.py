from django.contrib import admin
from .models import Alumno, Curso, NotaAlumnoCurso

@admin.register(Alumno)
class AlumnoAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre', 'apellido', 'email')
    search_fields = ('codigo', 'nombre', 'apellido')

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre', 'creditos')
    search_fields = ('codigo', 'nombre')

@admin.register(NotaAlumnoCurso)
class NotaAlumnoCursoAdmin(admin.ModelAdmin):
    list_display = ('alumno', 'curso', 'nota', 'fecha_registro')
    list_filter = ('curso', 'fecha_registro')
    search_fields = ('alumno__nombre', 'alumno__apellido', 'curso__nombre')