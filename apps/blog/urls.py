from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog, name='blog'),
    path('buscar_noticia/', views.buscar_noticia, name='buscar_noticia'),
]