from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# Главная страница
def index(request):    
    return HttpResponse('Главная страница')

# Страница со списком постов по группам
def group_posts(request, slug):
    return HttpResponse(f'Привет, я страница поста {slug}')