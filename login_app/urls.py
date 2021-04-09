
from django.urls import path#biblioteca que cria urls
from . import views
from login_app.views import login_sistema2
from django.contrib.auth import views as auth_views#importa as funções de autenticação e renomea para auth_views

urlpatterns = [
    #path('',views.login_sistema2, name='login_sistema2'),
    
    #path('', views.login_sistema2, name='login_sistema2')
    
    #path('',auth_views.LoginView.as_view(
    #template_name='arquivos_html_login/login.html'),name='login')
]
