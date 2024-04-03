from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cursos/', views.Cursos, name='cursos'),
    path('buscar_curso/', views.buscar_curso, name='buscar_curso')
]