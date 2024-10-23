from django.contrib import admin
from django.urls import path, include  # Импортируйте include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('myapp.urls')),  # Подключите URLs из myapp
]
