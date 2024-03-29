from django.shortcuts import render
from .models import Curso
from aluno.models import Aluno

def index(request):
    cursos = Curso.objects.order_by('-nota')
    alunos = Aluno.objects.order_by('-nome')

    return render(request, 'index.html', locals())
