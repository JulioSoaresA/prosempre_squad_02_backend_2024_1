from django.shortcuts import render
from .models import Curso, NossaHistoria, NossosValores
from aluno.models import Aluno

def index(request):
    cursos = Curso.objects.order_by('-nota')
    alunos = Aluno.objects.order_by('-nome')
    nossa_historia = NossaHistoria.objects.filter(ativo=True).last()
    return render(request, 'index.html', locals())

def Cursos(request):
    cursos = Curso.objects.order_by('-nota')
    ciencias_humanas = Curso.objects.filter(area_conhecimento='Ciências Humanas')
    ciencias_exatas = Curso.objects.filter(area_conhecimento='Ciências Exatas')
    Biociencias = Curso.objects.filter(area_conhecimento='Biociências')
    return render(request, 'cursos.html', locals())
