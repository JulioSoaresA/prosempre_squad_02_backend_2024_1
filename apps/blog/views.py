from django.shortcuts import render
from .models import Noticia

def blog(request):
    noticias = Noticia.objects.order_by('-data_publicacao')
    return render(request, 'blog/blog.html', locals())

def buscar_noticia(request):
    buscar = request.GET.get('buscar', None)
    if buscar:
        noticias = Noticia.objects.filter(titulo__icontains=buscar).order_by('-data_publicacao')
    else:
        noticias = Noticia.objects.order_by('-data_publicacao')
    return render(request, 'blog/blog.html', locals())
