from django.urls import path
from django.contrib import admin
from . import views  # Импортируйте ваши представления


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_view, name='home'),  # Новый маршрут для главной страницы
    #path('', views.data_view),  # Перенаправляем корневой URL на представление data_view
    path('data/', views.data_view, name='data'),  # URL для страницы data
    path('test/', views.test_view, name='test'),  # URL для страницы test

]
