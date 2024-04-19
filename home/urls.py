from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='rich_text'),
    path('salvar/', views.salvar, name='salvar')
]
