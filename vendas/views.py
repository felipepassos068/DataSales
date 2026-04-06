from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'vendas/home.html')

def register(request):
    return render(request, 'vendas/register.html')

def consult(request):
    return render(request, 'vendas/consult.html')

def relatorio(request):
    return render(request, 'vendas/relatorio.html')