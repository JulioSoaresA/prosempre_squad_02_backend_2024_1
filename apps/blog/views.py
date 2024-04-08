from django.shortcuts import render
from .models import Noticia
from django.shortcuts import get_object_or_404

def blog(request):
    noticias = Noticia.objects.order_by('-data_publicacao')
    return render(request, 'blog/blog.html', locals())

def blog_post_individual(request, noticia_id):
    noticia = get_object_or_404(Noticia, id=noticia_id)
    return render(request, 'blog/postindividual.html', locals())

def buscar_noticia(request):
    buscar = request.GET.get('buscar', None)
    if buscar:
        noticias = Noticia.objects.filter(titulo__icontains=buscar).order_by('-data_publicacao')
    else:
        noticias = Noticia.objects.order_by('-data_publicacao')
    return render(request, 'blog/blog.html', locals())

def blog_individual(request, blog_id):
    noticia = Noticia.objects.filter(id=blog_id)
    return render(request, 'blog/blog_individual.html', locals())