
from django.shortcuts import render, get_object_or_404, redirect, get_list_or_404
from django.http import HttpResponse
from urllib import request
from .forms import Postform, PostMateria, Prova, User_create #ESTA É A CLASSE QUE FOI CRIADA LÁ NO ARQUIVO forms.py
from django.utils import timezone
from .models import Post, Login_sistema, Materia

from django.contrib.auth import authenticate, login, logout #Estas bibliotecas são responsáveis pelos logins;
from django.contrib.auth.decorators import login_required  #biblioteca para verificar se um user está autenticado;

from django.contrib.auth import views as auth_views #aqui estou importando as views de URLs do django e renomeando para auth_views 

###### usando as views genéricas do django ! ########
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import ListView, TemplateView
from django.urls import reverse_lazy

####### permissões para grupos ######
from braces.views import GroupRequiredMixin

####### Cadastro de usuários  ########
from django.contrib.auth.models import User #bibliotecas que cuidam de criar usuer e super users

    
def sobre(request):
    return render(request, 'arquivos_html/sobre.html')

def registros(request):
    return render(request, 'arquivos_html/registros.html')

@login_required(login_url='login_sistema',redirect_field_name='meu_redirecionamento')

def detalhe_post(request,pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'arquivos_html/detalhe_post.html', {'post' : post})

@login_required(login_url='login_sistema', redirect_field_name='meu_redirecionamento')

#def post_delete(request, pk):
# post = get_object_or_404(Post, pk=pk)
# post.delete()
#return redirect('lista_post')

#@login_required(login_url='login_sistema', redirect_field_name='Meu_redirecionamento')

#def xxxxxx(request, pk):
#pk = pk
# return render(request, 'arquivos_html/teste2.html',{'pk':pk} )

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

def xxxx(request):#as instruções dessas funções que irá fazer consultas no banco.
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
    
        """if request.method == "POST":
            form = PostLogin(request.POST)
        
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('lista_post')
            else:
                return redirect('login_sistema')
        return render(request, 'arquivos_html/login.html')"""
        
        return redirect('login')
        

def logout_sistema(request):
    logout(request)
    return redirect('login_sistema')

class Teste_class(GroupRequiredMixin,TemplateView):
    group_required = u'administrador'
    template_name = 'arquivos_html/teste_class.html'
    
class xxxxxx(CreateView):
    fields = ['nome','nota','descricao']
    success_url = reverse_lazy('lista_post')
    model = Materia
    template_name = 'arquivos_html/criar_materia.html'
    
    def form_valid(self, form):
        form.instance.usuario = self.request.user
        url = super().form_valid(form)
        return url
    
    
    
    
def nova_prova(request):
    if request.method == "POST":
        form = Postprova(request.POST)
        
        if form.is_valid():
            post = form.save(commit=False)
            #post.post = request.POST['post']
            post.data = timezone.now()
            post.usuario = request.user
            
            post.save()
            return redirect('lista_post')
    else:
        form = Postprova()
        titulo2 = 'Criar provaaaaaaa'
    return render(request, 'arquivos_html/criar_materia.html',{'form':form})


@login_required(redirect_field_name='meu_redirecionamento', login_url='login_sistema')
def nova_materia(request):
    if request.method == "POST":
        form = PostMateria(request.POST)
        
        if form.is_valid():
            post = form.save(commit=False)
            #post.post = request.POST['post']
            
            post.nome = request.POST['nome']
            post.nota = request.POST['nota']
            post.descricao = request.POST['descricao']
            post.usuario = request.user
            """def form_valid(self, form):
                form.instance.usuario = self.request.user
                url = super().form_valid(form)
                return url"""
            
            post.save()
            return redirect('lista_post')
    else:
        form = PostMateria()
    return render(request, 'arquivos_html/criar_materia.html',{'form' : form})

@login_required(redirect_field_name='meu_redirecionamento', login_url='login_sistema')
def lista_post(request):
    posts = Materia.objects.filter(usuario=request.user) #aqui pela os dados que pertecem somente ao usuario que está logado.
    #return render(request, 'arquivos_html/lista_post.html', {'posts': posts})
    return render(request, 'arquivos_html/materias.html', {'posts':posts})

def post_edit_materia(request, pk): #função para editar um post
     
     post = get_object_or_404(Materia, pk=pk, usuario=request.user)#usuario=request.user é um filtro para que apenas o user autenticado faça alterações no objeto requisitado
     if request.method == "POST":
         form = PostMateria(request.POST, instance=post)
         if form.is_valid():
             post = form.save(commit=False)
             
             post.author = request.user
             post.published_date = timezone.now()
             
             post.save()
             return redirect('detalhe_post', pk=post.pk)
     else:
         form = PostMateria(instance=post)
     return render(request, 'arquivos_html/edit_post.html', {'form': form})


@login_required(login_url='login_sistema', redirect_field_name='Meu_redirecionamento')
def postConfirmDelete(request, pk):
    post = get_object_or_404(Materia, pk=pk, usuario=request.user)#usuario=request.user é um parâmetro para verificar se a requisição faz parte de um post do user autenticado.
    pk = pk
    return render(request, 'arquivos_html/delete_confirm.html',{'pk':pk})

@login_required(login_url='login_sistema', redirect_field_name='Meu_redirecionamento')
def postMateriaDelete(request, pk):
    post = get_object_or_404(Materia, pk=pk, usuario=request.user)
    post.delete()
    return redirect('lista_post')

class Nova_materia2(CreateView):
    template_name = 'arquivos_html/form.html'
    model = Materia
    fields = ['nome', 'nota','descricao']
    success_url = reverse_lazy('lista_post')
    
    def form_valid(self, form):
        form.instance.usuario = self.request.user
        url = super().form_valid(form)
        return url
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo_pag'] = "Criar Matéria"
        context['botao'] = "Cadastrar"
        return context


class Edit_materia(UpdateView):
    template_name = 'arquivos_html/form.html'
    model = Materia
    fields = ['nome', 'nota', 'descricao']
    success_url = reverse_lazy('lista_post')
    
    def get_object(self, queryset=None):
        self.object = get_object_or_404(Materia, pk=self.kwargs['pk'], usuario=self.request.user)
        
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo_pag'] = "Edição de Matéria"
        context['botao'] = "Salvar"
        return context
    

class List_materias(ListView):
    template_name = 'arquivos_html/materias.html'
    model = Materia

class Nova_prova(CreateView):
    template_name = 'arquivos_html/form.html'
    model = Prova
    fields = ['materia', 'arquivo']
    success_url = reverse_lazy('lista_post')
    
    def form_valid(self, form):
        form.instance.data = self.timezone.now()
        url = super().form_valid(form)
        return url
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo_pag'] = "Criar Prova"
        return context
    
        
class List_prova(ListView):
    template_name = 'arquivos_html/lista_prova.html'
    model = Prova
    
class Create_user(CreateView):
    template_name = 'arquivos_html/form.html'
    success_url = reverse_lazy('lista_post')
    form_class = User_create

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo_pag'] = "Cadastrar usuário"
        context['botao'] = "Cadastrar"
        return context





