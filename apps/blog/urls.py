from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog, name='blog'),
    path('<int:noticia_id>', views.blog_post_individual, name='blog_post_individual'),
    path('buscar_noticia/', views.buscar_noticia, name='buscar_noticia'),
]