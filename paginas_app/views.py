from django.shortcuts import render
from django.http import HttpResponse
from urllib import request
# Create your views here.


def index(request):
    """
    docstring
    """
    return render(request, 'arquivos_html/base.html')
    
def sobre(request):
    """
    docstring
    """
    return render(request, 'arquivos_html/sobre.html')










def teste2(request):
    """
    docstring
    """
    return HttpResponse('<h1>TEste</h1>')
