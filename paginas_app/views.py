from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from urllib import request
from .forms import Postform #ESTA É A CLASSE QUE FOI CRIADA LÁ NO ARQUIVO forms.py
from django.utils import timezone
from django.shortcuts import redirect
from .models import Post
# Create your views here.

    
def sobre(request):
    return render(request, 'arquivos_html/sobre.html')

def registros(request):
    return render(request, 'arquivos_html/registros.html')

def login(request):
    return render(request, 'arquivos_html/login.html')

def detalhe_post(request,pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'arquivos_html/detalhe_post.html', {'post' : post})


def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('lista_post')



def post_new(request):
    if request.method == "POST":
        form = Postform(request.POST)
        
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('detalhe_post', pk=post.pk)
    else:
        form = Postform()
    return render(request, 'arquivos_html/edit_post.html',{'form' : form})

def post_edit(request, pk): #função para editar um post
     post = get_object_or_404(Post, pk=pk)
     if request.method == "POST":
         form = Postform(request.POST, instance=post)
         if form.is_valid():
             post = form.save(commit=False)
             post.author = request.user
             post.published_date = timezone.now()
             post.save()
             return redirect('detalhe_post', pk=post.pk)
     else:
         form = Postform(instance=post)
     return render(request, 'arquivos_html/edit_post.html', {'form': form})

def lista_post(request):#as instruções dessas funções que irá fazer consultas no banco.
    posts = Post.objects.order_by('-created_date')
    cont = len(posts)
    #return render(request, 'arquivos_html/lista_post.html', {'posts': posts})
    return render(request, 'arquivos_html/listar2.html', {'posts':posts, 'cont':cont})

    
def listar2(request):
    return render(request,'arquivos_html/listar2.html')



def teste2(request):
    """
    docstring
    """
    return render(request, 'arquivos_html/teste2.html')

def teste_delete(request, pk):
    pk = pk
    return render(request, 'arquivos_html/teste2.html',{'pk':pk} )
