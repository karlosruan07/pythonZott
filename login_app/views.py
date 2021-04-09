
from django.shortcuts import render
from django.http import HttpResponse
from urllib import request
from django.shortcuts import redirect
from paginas_app.forms import Postform, PostLogin
from django.contrib.auth import authenticate, login

from django.contrib.auth import views as auth_views

"""path('',auth_views.LoginView.as_view(
    template_name='arquivos_html_login/login.html'),name='login')"""
