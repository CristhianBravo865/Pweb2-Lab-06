from django import forms
from .models import Alumno, Curso, NotaAlumnoPorCurso

class AlumnoForm(forms.ModelForm):
    class Meta:
        model = Alumno
        fields = ['nombre', 'apellido', 'CUI']

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['nombre', 'descripcion']

class NotaAlumnoPorCursoForm(forms.ModelForm):
    class Meta:
        model = NotaAlumnoPorCurso
        fields = ['alumno', 'curso', 'nota']
