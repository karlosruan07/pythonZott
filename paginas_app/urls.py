
from django.urls import path
from . import views
from paginas_app.views import index, teste2

urlpatterns = [
    path('', views.index, name='index'),
    path('teste2/', views.teste2)#não esquecer da barra para completar a url
    
]