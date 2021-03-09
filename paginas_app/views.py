from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from urllib import request
from .forms import Postform, PostLogin #ESTA É A CLASSE QUE FOI CRIADA LÁ NO ARQUIVO forms.py
from django.utils import timezone
from django.shortcuts import redirect
from .models import Post, Login_sistema
from django.contrib.auth.models import User,UserManager #bibliotecas que cuidam de criar usuer e super users
from django.contrib.auth import authenticate, login, logout #Estas bibliotecas são responsáveis pelos logins;
from django.contrib.auth.decorators import login_required #biblioteca para verificar se um user está autenticado;
# Create your views here.

    
def sobre(request):
    return render(request, 'arquivos_html/sobre.html')

def registros(request):
    return render(request, 'arquivos_html/registros.html')

@login_required(login_url='login_sistema',redirect_field_name='meu_redirecionamento')

def detalhe_post(request,pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'arquivos_html/detalhe_post.html', {'post' : post})

@login_required(login_url='login_sistema', redirect_field_name='meu_redirecionamento')

def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('lista_post')

@login_required(login_url='login_sistema', redirect_field_name='Meu_redirecionamento')

def post_delete_confirm(request, pk):
    pk = pk
    return render(request, 'arquivos_html/teste2.html',{'pk':pk} )

@login_required(login_url='login_sistema', redirect_field_name='meu_redirecionamento')
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

@login_required(login_url='login_sistema', redirect_field_name='Meu_redirecionamento')#esse parêmetro (meu_redirecionamento)substitui o método next na url, e o login url serve para redirecionar para a página de login.

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

@login_required(redirect_field_name='meu_redirecionamento', login_url='login_sistema')#esse parêmetro (meu_redirecionamento)substitui o método next na url, e o login url serve para redirecionar para a página de login.

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




def create_user(request):
    """Esta função cria um usuário comum"""
    user = User.objects.create_user('user_teste','user_teste@gmail.com', 'user_teste_password')
    
    user.save()
    #return render(request,'arquivos_html/create_user.html')
    
def create_super_user(request):
    """Esta função cria um super_usuario"""
    super_user = User.objects.create_superuser('super_user','superuser@gmail.com','super_user_password')
    super_user.save()
    
def alter_password(request):
    """Esta função altera a senha de um usuário"""
    user_alter_password = User.objects.get(username='user_teste')
    user_alter_password.set_password('user_teste_new_password')
    
    user_alter_password.save()
    
def authentication(request):
    """verifica as credenciais de um usurário"""
    user_authentication = authenticate(username='user_teste',password = 'user_teste_new_password')
    if(user_authentication is not None):
        #se u user e a password estiverem corretas, executa isso
        return redirect('youtube.com')
    else:
        return redirect('login')

def login_sistema(request):
    
    """esta função primeiro valida um login, senão validar o login então ela retorna a página de login para se autenticar"""
    if(request.user.is_authenticated):
        #se u user e a password estiverem corretas, executa isso
        return redirect('lista_post')
    
    else:
    
        if request.method == "POST":
            form = PostLogin(request.POST)
        
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('lista_post')
            else:
                return redirect('login_sistema')
        return render(request, 'arquivos_html/login.html')

def logout_sistema(request):
    logout(request)
    return redirect('login_sistema')

"""def post_new(request):
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
    return render(request, 'arquivos_html/edit_post.html',{'form' : form})"""
