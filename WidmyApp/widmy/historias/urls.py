from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
       path('<int:documento>/', views.historia_view, name='historia_view'),
]
