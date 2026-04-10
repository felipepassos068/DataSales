from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('produtos/', views.lista_produtos, name='lista_produtos'),
    path('produtos/criar/', views.criar_produto, name='criar_produto'),
    path('produtos/editar/<int:id>/', views.editar_produto, name='editar_produto'),
    path('produtos/deletar/<int:id>/', views.deletar_produto, name='deletar_produto'),
    path('vendas/', views.lista_vendas, name='lista_vendas'),
    path('vendas/criar/', views.criar_venda, name='criar_venda'),
    path('editar-venda/<int:id>/', views.editar_venda, name='editar_venda'),
    path('api/dashboard/', views.dados_dashboard, name='dados_dashboard'),
    path('dashboard/', views.dashboard, name='dashboard'), 
]