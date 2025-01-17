from django.http import HttpResponse
from django.shortcuts import render

def home_view(request):
    return render(request, 'myapp/index.html')

def data_view(request):
    return HttpResponse("<h1>Это страница Data</h1><p>Содержимое для страницы Data.</p>")

def test_view(request):
    return HttpResponse("<h1>Это страница Test</h1><p>Содержимое для страницы Test.</p>")

def new(request):
    return render(request, 'myapp/new.html')



