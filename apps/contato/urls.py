from django.urls import path, include
from . import views


urlpatterns = [
    path('contato/', views.contato, name='contato'),
]
