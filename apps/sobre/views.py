from django.shortcuts import render
from .models import Equipe

def sobre(request):
    equipe = Equipe.objects.all()
    return render(request,'sobre/sobre.html', locals())