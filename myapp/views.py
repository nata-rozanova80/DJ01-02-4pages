from django.http import HttpResponse

def home_view(request):
    return HttpResponse("<h1>Добро пожаловать на главную страницу!</h1>")

def data_view(request):
    return HttpResponse("<h1>Это страница Data</h1><p>Содержимое для страницы Data.</p>")

def test_view(request):
    return HttpResponse("<h1>Это страница Test</h1><p>Содержимое для страницы Test.</p>")


