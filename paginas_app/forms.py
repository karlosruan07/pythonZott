
from django import forms
from .models import Post, Login_sistema

class Postform(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','text','pontos')
        
class PostLogin(forms.ModelForm):
    class Meta:
        model = Login_sistema
        fields = ('username', 'password')
