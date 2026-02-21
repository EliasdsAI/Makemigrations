from django.shortcuts import render

from categoria.models import Categoria
from produto.models import Produto


# Create your views here.

def inicio(request):
    return render(request, 'home.html')

def historia(request):
    return render(request, 'historia.html')

def administrativo(request):
    return render(request,'menuadm.html')

def sushi(request):
    sushi =Categoria.objects.get(nome='sushi')
    produtos = Produto.objects.filter(categoria=sushi)
    return render(request, "sushi.html",{'produtos': produtos})

def temaki(request):
    temaki =Categoria.objects.get(nome='temaki')
    produtos = Produto.objects.filter(categoria=temaki)
    return render(request, "temaki.html",{'produtos': produtos})

def sobremesa(request):
    sobremesa =Categoria.objects.get(nome='sobremesa')
    produtos = Produto.objects.filter(categoria=sobremesa)
    return render(request, "sobremesa.html",{'produtos': produtos})

def sashimi(request):
    sashimi =Categoria.objects.get(nome='sashimi')
    produtos = Produto.objects.filter(categoria=sashimi)
    return render(request, "sashimi.html",{'produtos': produtos})

def bebidas(request):
    bebidas =Categoria.objects.get(nome='bebidas')
    produtos = Produto.objects.filter(categoria=bebidas)
    return render(request, "bebidas.html",{'produtos': produtos})

def home(request):
    return render(request, 'home.html')

def contatos(request):
    return render(request, 'contatos.html')

def diversos(request):
    diversos =Categoria.objects.get(nome='diversos')
    produtos = Produto.objects.filter(categoria=diversos)
    return render(request, "sashimi.html",{'produtos': produtos})

def menucli(request):
    return render(request, 'menucliente.html')
