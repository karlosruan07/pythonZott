
from django.urls import path
from . import views
from paginas_app.views import index

urlpatterns = [
    path('', views.index, name='index'),
    
]