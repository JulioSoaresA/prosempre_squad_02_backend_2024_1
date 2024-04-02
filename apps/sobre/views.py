from django.shortcuts import render
from .models import Equipe
from curso.models import Curso, NossaHistoria, NossosValores

def sobre(request):
    equipe = Equipe.objects.all()
    nossa_historia = NossaHistoria.objects.filter(ativo=True).first()
    nossos_valores = NossosValores.objects.filter(ativo=True).first()
    return render(request,'sobre/sobre.html', locals())

