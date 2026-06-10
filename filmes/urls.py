from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_filmes, name='lista_filmes'),
    path('adicionar/', views.adicionar_filme, name='adicionar_filme'),
    path('editar/<int:id>/', views.editar_filme, name='editar_filme'),
    path('excluir/<int:id>/', views.excluir_filme, name='excluir_filme'),
]