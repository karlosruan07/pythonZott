
from django.urls import path
from . import views
from paginas_app.views import teste2, sobre, registros, login, post_new, detalhe_post, post_edit, lista_post, listar2, teste_delete

urlpatterns = [
    path('', views.lista_post, name='lista_post'),
    path('teste2/', views.teste2),#não esquecer da barra para completar a url
    path('sobre/', views.sobre, name='sobre'),
    path('registros/',views.registros, name='registros'),
    path('login/', views.login, name='login'),
    path('post/new/', views.post_new, name='post_new'),
    
    path('post/<int:pk>/', views.detalhe_post, name='detalhe_post'),
    
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    
    path('post/<int:pk>/delete/',views.post_delete, name='post_delete'),
    
    path('listar2/', views.listar2, name='listar2'),
    
    path('post/<int:pk>/teste_delete/',views.teste_delete,name='teste_delete'),
    
]