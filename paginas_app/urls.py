
from django.urls import path
from . import views
from paginas_app.views import teste2, sobre, registros, login_sistema , post_new, detalhe_post, post_edit, lista_post, listar2, create_user, create_super_user, alter_password, authentication, logout_sistema, post_delete, post_delete_confirm

urlpatterns = [
    path('lista_post', views.lista_post, name='lista_post'),
    path('teste2/', views.teste2),#não esquecer da barra para completar a url
    path('sobre/', views.sobre, name='sobre'),
    path('registros/',views.registros, name='registros'),
    
    
    
    path('post/new/', views.post_new, name='post_new'),
    
    path('post/<int:pk>/', views.detalhe_post, name='detalhe_post'),
    
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    
    path('post/<int:pk>/delete/',views.post_delete, name='post_delete'),########
    
    path('listar2/', views.listar2, name='listar2'),
    
    path('post/<int:pk>/post_delete_confirm/',views.post_delete_confirm,name='post_delete_confirm'),
    
    path('post/create_user/', views.create_user, name='create_user'),
    
    path('post/create_super_user/', views.create_super_user, name='create_super_user'),
 
    path('post/alter_password/', views.alter_password , name='alter_password'),
    
    path('post/authentication/',views.authentication, name='authentication' ),
    
    path('', views.login_sistema, name='login_sistema'),
    
    path('logout/', views.logout_sistema, name='logout_sistema'),
]



