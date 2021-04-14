
from django import forms
from django.contrib.auth.models import User
from .models import Post, Login_sistema, Materia, Prova
from django.core.exceptions import ValidationError #biblioteca de validação de formulário
from django.contrib.auth.forms import UserCreationForm

class Postform(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('materia','title','text','pontos')
        
class PostMateria(forms.ModelForm):
        class Meta:
            model = Materia
            fields = ('nome', 'nota', 'descricao')
            
class Postprova(forms.ModelForm):
    class Meta:
        model = Prova
        fields = ('materia','arquivo')       
            
class PostLogin(forms.ModelForm):
    class Meta:
        model = Login_sistema
        fields = ('username', 'password')

class User_create(UserCreationForm):
    email = forms.EmailField(max_length=100)#requisto obrigatorio do email
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2'] #password1 e password2 é para colocar a senha e confirmar ela.
    
    def clean_email(self):
        e = self.cleaned_data['email']#pega o objeto email da lista da classe User acima
        if User.objects.filter(email=e).exists():
            raise ValidationError(f"O email {e} já existe.")

        return e