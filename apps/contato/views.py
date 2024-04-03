from django.shortcuts import render
from .models import Contato

def contato(request):
    if request.method == 'POST':
        novo_contato = Contato()
        novo_contato.assunto = request.POST.get('assunto')
        novo_contato.nome = request.POST.get('nome')
        novo_contato.email = request.POST.get('email')
        novo_contato.mensagem = request.POST.get('mensagem')
        novo_contato.save()
    return render(request,'contato/contato.html', locals())