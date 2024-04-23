from django.http import HttpResponse
from django.shortcuts import render
import json
from .models import Texto

def home(request):
    texto = Texto.objects.all()
    return render(request, 'home.html', {'textos': texto})

def salvar(request): 
    data = json.loads(request.body)
    texto = Texto(conteudo_texto=data['texto'])
    texto.save()
    return HttpResponse('1') #Retorna 1 se o processo deu certo