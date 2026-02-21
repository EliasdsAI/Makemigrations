"""
URL configuration for app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import inicio, historia, administrativo, sushi, temaki, sobremesa, sashimi, bebidas, contatos, diversos, \
    menucli
from . import views

urlpatterns = [
    path('',inicio),
    path('historia/', historia, name='historia'),
    path('administrativo/', administrativo, name='administrativo'),
    path('sushi/', sushi, name='sushi'),
    path('temaki/', temaki, name='temaki'),
    path('sobremesa/', sobremesa, name='sobremesa'),
    path('sashimi/', sashimi, name='sashimi'),
    path('bebidas/', bebidas, name='bebidas'),
    path('home/', views.home, name='home'),
    path('contatos/', contatos, name='contatos'),
    path('diversos/', diversos, name='diversos'),
    path('menucli/', menucli, name='menucli'),

]
