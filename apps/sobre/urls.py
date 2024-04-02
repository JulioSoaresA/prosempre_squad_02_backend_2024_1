from django.urls import path, include
from . import views


urlpatterns = [
    path('sobre/', views.sobre, name='sobre')
]
