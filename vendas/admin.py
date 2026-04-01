from django.contrib import admin
from .models import Produto, Venda, Vendedor


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'categoria', 'preco', 'quantidade_estoque')
    search_fields = ('nome', 'categoria')


@admin.register(Vendedor)
class VendedorAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)


@admin.register(Venda)
class VendaAdmin(admin.ModelAdmin):
    list_display = ('id', 'produto', 'vendedor', 'quantidade', 'valor_total', 'data_venda')
    list_filter = ('data_venda', 'produto', 'vendedor')
    readonly_fields = ('valor_unitario', 'valor_total', 'data_venda')