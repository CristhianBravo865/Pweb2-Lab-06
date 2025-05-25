from django.urls import path
from . import views

urlpatterns = [
    path('alumnos/', views.lista_alumnos, name='lista_alumnos'),
    path('alumnos/nuevo/', views.crear_alumno, name='crear_alumno'),

    path('cursos/', views.lista_cursos, name='lista_cursos'),
    path('cursos/nuevo/', views.crear_curso, name='crear_curso'),

    path('notas/', views.lista_notas, name='lista_notas'),
    path('notas/nuevo/', views.crear_nota, name='crear_nota'),
    
    path('', views.home, name='home'),  # esta línea para el path vacío
    path('alumnos/', views.lista_alumnos, name='lista_alumnos'),

    path('alumnos/nuevo/', views.crear_alumno, name='crear_alumno'),
    path('alumnos/', views.lista_alumnos, name='lista_alumnos'),
]