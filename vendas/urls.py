from django.urls import path
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    path('', RedirectView.as_view(url='home/', permanent=True)),

    path('home/', views.home, name='home'),
    path('registrar/', views.register, name='registrar'),
    path('consultar/', views.consult, name='consultar'),
    path('consultar/produtos/', views.lista_produtos, name='lista_produtos'),
    path('registrar/produto/', views.criar_produto, name='criar_produto'),
    path('produtos/editar/<int:id>/', views.editar_produto, name='editar_produto'),
    path('produtos/deletar/<int:id>/', views.deletar_produto, name='deletar_produto'),
    path('consultar/vendas/', views.lista_vendas, name='lista_vendas'),
    path('registrar/venda/', views.criar_venda, name='criar_venda'),
    path('editar-venda/<int:id>/', views.editar_venda, name='editar_venda'),
    path('api/dashboard/', views.dados_dashboard, name='dados_dashboard'),
    path('dashboard/', views.dashboard, name='dashboard'), 
]