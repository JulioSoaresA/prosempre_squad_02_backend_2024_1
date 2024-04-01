from django.shortcuts import render
from .models import Curso, NossaHistoria, NossosValores
from aluno.models import Aluno

def index(request):
    cursos = Curso.objects.order_by('-nota')
    alunos = Aluno.objects.order_by('-nome')
    nossa_historia = NossaHistoria.objects.filter(ativo=True).last()
    return render(request, 'index.html', locals())
