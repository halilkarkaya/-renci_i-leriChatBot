from django.contrib import admin
from django.urls import path, include
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),  # Uygulamanın urls.py dosyasını dahil et
    path('cevap_al/', views.cevap_al, name='cevap_al')  # RAG yanıtını almak için URL
]
