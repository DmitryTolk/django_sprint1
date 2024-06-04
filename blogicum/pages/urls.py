# Импортируем функцию path()
# и файл pages/views.py, в котором объявлена view-функция index().
from django.urls import path

from . import views

app_name = 'pages'

urlpatterns = [
    # Вызывается view-функция about() из файла views.py
    path('about/', views.about, name='about'),
    # Вызывается view-функция abrulesout() из файла views.py
    path('rules/', views.rules, name='rules'),
]
