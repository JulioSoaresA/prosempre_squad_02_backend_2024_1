from django.shortcuts import render
from .models import Equipe
# Create your views here.


def sobre(request):
    return render(request,'sobre.html', locals())