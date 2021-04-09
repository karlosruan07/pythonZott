
from django.urls import path
from . import views
from paginas_app.views import teste2, sobre, registros, login_sistema, post_new, detalhe_post, post_edit, lista_post, listar2, create_user, create_super_user, alter_password, authentication, logout_sistema, Nova_prova, nova_materia, post_edit_materia, postConfirmDelete, postMateriaDelete, Nova_materia2, List_materias, Edit_materia, Create_user

from django.contrib.auth import views as auth_views #aqui estou renomeando a view para auth_views, essa view é a base para mudar a senha, fazer login, logout ...etc.

urlpatterns = [
    path('lista_post', views.lista_post, name='lista_post'),
    path('teste2/', views.teste2),#não esquecer da barra para completar a url
    path('sobre/', views.sobre, name='sobre'),
    path('registros/',views.registros, name='registros'),
    
    
    
    path('post/new/', views.post_new, name='post_new'),
    
    path('post/<int:pk>/', views.detalhe_post, name='detalhe_post'),
    
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
        
    path('listar2/', views.listar2, name='listar2'),
    
    path('post/create_user/', views.create_user, name='create_user'),
    
    path('post/create_super_user/', views.create_super_user, name='create_super_user'),
 
    path('post/alter_password/', views.alter_password , name='alter_password'),
    
    path('post/authentication/',views.authentication, name='authentication' ),
    
    path('',views.login_sistema, name='login_sistema'),
    
    #########  A url de login fica nos settings como uma contante. ##########
    
    #########  A url de logout fica nos settings como uma contante. ##########
    
    path('change_password/', auth_views.PasswordChangeView.as_view(template_name='arquivos_html/change_password.html'),name='change_password'),#formulario para mudar a senha

    path('accounts/password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='arquivos_html/password_change_done.html')),#Pagina de confirmação de alteração da senha
    
    path('accounts/password_reset/', auth_views.PasswordResetView.as_view(template_name='arquivos_html/reset_password.html'), name='reset_password'),
    
    path('nova_prova/', views.Nova_prova.as_view(), name='nova_prova'),
    
    path('nova_materia/', views.nova_materia, name='nova_materia'),
    
    
    #URLs DA DAS MATERIAS
    path('post_edit_materia/<int:pk>/', views.post_edit_materia, name='post_edit_materia'),
    
    path('postMateriaDelete/<int:pk>/',views.postMateriaDelete, name='postMateriaDelete'),
    
    path('postConfirmDelete/<int:pk>/', views.postConfirmDelete,name='postConfirmDelete'),
    
    path('nova_materia_2/',views.Nova_materia2.as_view(), name='nova_materia_2'),
    
    path('lista_materias/', views.List_materias.as_view(), name='List_materias'),
    
    path('edit_materia/<int:pk>/', views.Edit_materia.as_view(), name='edit_materia'),

    path('registrar/', views.Create_user.as_view(), name='registrar'),   
]