from django.shortcuts import render
from django.http import HttpResponse
from urllib import request
# Create your views here.


def index(request):
    """
    docstring
    """
    return render(request, 'arquivos_html/index.html')
    