from django.shortcuts import render
from .models import Curso, NossaHistoria, NossosValores
from aluno.models import Aluno

def index(request):
    cursos = Curso.objects.all()
    alunos = Aluno.objects.order_by('-nome')
    nossa_historia = NossaHistoria.objects.filter(ativo=True).last()
    return render(request, 'home/home.html', locals())

def Cursos(request):
    cursos = Curso.objects.order_by('-nota')
    ciencias_humanas = Curso.objects.filter(area_conhecimento='Ciências humanas')
    ciencias_exatas = Curso.objects.filter(area_conhecimento='Ciências exatas')
    biociencias = Curso.objects.filter(area_conhecimento='Biociências')
    return render(request, 'cursos/cursos.html', locals())

def buscar_curso(request):
    buscar = request.GET.get('buscar', None)
    if buscar:
        cursos = Curso.objects.filter(nome__icontains=buscar).order_by('nome')
        ciencias_humanas = Curso.objects.filter(area_conhecimento='Ciências humanas', nome__icontains=buscar)
        ciencias_exatas = Curso.objects.filter(area_conhecimento='Ciências exatas', nome__icontains=buscar)
        biociencias = Curso.objects.filter(area_conhecimento='Biociências', nome__icontains=buscar)
    else:
        cursos = Curso.objects.order_by('nome')
    return render(request, 'cursos/cursos.html', locals())