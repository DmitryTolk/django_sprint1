from django.urls import path

from . import views

app_name = 'blog'

urlpatterns = [
    # Вызывается view-функция index() из файла views.py
    path('', views.index, name='index'),
    # Вызывается view-функция post_detail() из файла views.py
    path('posts/<int:id>/', views.post_detail, name='post_detail'),
    # Вызывается view-функция category_posts() из файла views.py
    path('category/<slug:category_slug>/', views.category_posts,
         name='category_posts'),
]
