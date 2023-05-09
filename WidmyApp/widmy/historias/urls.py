from django.contrib import admin
from django.urls import path
from . import views
#Editando esto para wue salga en el commit
urlpatterns = [
       path('buscar/', views.opciones_view, name='opciones_view'),
       path('<int:documento>/', views.historia_view, name='historia_view'),
]
