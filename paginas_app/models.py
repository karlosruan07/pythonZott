from django.db import models
from django.conf import settings
from django.utils import timezone
from django import forms
from django.contrib.auth.models import User

# Create your models here.

class Materia(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)
    nome = models.CharField(blank=False, max_length=100)
    nota = models.DecimalField(decimal_places=1, max_digits=2)
    descricao = models.TextField(blank=False, max_length=200)
    
    def __str__(self):
        """
        docstring
        """
        return "{}".format(self.nome)

class Post(models.Model):
    materia = models.ForeignKey(Materia, on_delete=models.PROTECT)
    
    #author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) #on_delete=models.PROTECT para proteger arquivos que estejam sendo usados em outras situações
    
    title = models.CharField(max_length=200)# título da publicação    se caso o nome da variavel estiver aparecendo no site estranho então temos que passar como parâmetros tambem o (verbose_name="nome_da variavel normal pt_br")
    text = models.TextField()# pega o texto publicação, como está sem os parâmetros então não tem limites.
# o atributo unique=True serve para um campo ser unico, não pode se repetir.
    created_date = models.DateTimeField(default=timezone.now)#pega a hora e a hora da publicação
    pontos = models.DecimalField(decimal_places=1, max_digits=2)#pega valores em float
    published_date = models.DateTimeField(blank=True, null=True) #linkando para outro modelo
    
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)
    def __str__(self):
        """
        docstring
        """
        return "{}".format(self.title)
    
class Prova(models.Model):
    materia = models.ForeignKey(Materia, on_delete=models.PROTECT)
    arquivo = models.FileField(upload_to='pdf/')
    
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)
    
    
#terá um campo para a importação de arquivos.

    
class Login_sistema(models.Model):
    username = models.TextField()
    password = models.TextField()
    