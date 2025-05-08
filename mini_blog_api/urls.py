from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),  # Перенаправление корневого URL на приложение blog
]

# Starting development server at http://127.0.0.1:8000/