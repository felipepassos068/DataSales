from django.shortcuts import render, redirect, get_object_or_404
from .models import Produto, Venda, Vendedor



def home(request):
    return render(request, 'vendas/home.html')



def lista_produtos(request):
    nome = request.GET.get('nome')
    marca = request.GET.get('marca')

    produtos = Produto.objects.all()

    if nome:
        produtos = produtos.filter(nome__icontains=nome)

    if marca:
        produtos = produtos.filter(marca__icontains=marca)

    return render(request, 'vendas/produtos.html', {
        'produtos': produtos
    })



def criar_produto(request):
    if request.method == 'POST':
        Produto.objects.create(
            nome=request.POST.get('nome'),
            marca=request.POST.get('marca'),
            preco=request.POST.get('preco'),
            quantidade_estoque=request.POST.get('quantidade')
        )
        return redirect('lista_produtos')

    return render(request, 'vendas/criar_produto.html')



def editar_produto(request, id):
    produto = get_object_or_404(Produto, id=id)

    if request.method == 'POST':
        produto.nome = request.POST.get('nome')
        produto.marca = request.POST.get('marca')
        produto.preco = request.POST.get('preco')
        produto.quantidade_estoque = request.POST.get('quantidade')
        produto.save()

        return redirect('lista_produtos')

    return render(request, 'vendas/editar_produto.html', {
        'produto': produto
    })



def deletar_produto(request, id):
    produto = get_object_or_404(Produto, id=id)
    produto.delete()
    return redirect('lista_produtos')



def lista_vendas(request):
    vendas = Venda.objects.select_related('produto', 'vendedor').all()

    return render(request, 'vendas/vendas.html', {
        'vendas': vendas
    })



def criar_venda(request):
    produtos = Produto.objects.all()
    vendedores = Vendedor.objects.all()

    if request.method == 'POST':
        produto_id = request.POST.get('produto')
        vendedor_id = request.POST.get('vendedor')
        quantidade = int(request.POST.get('quantidade'))

        produto = get_object_or_404(Produto, id=produto_id)
        vendedor = get_object_or_404(Vendedor, id=vendedor_id)

        Venda.objects.create(
            produto=produto,
            vendedor=vendedor,
            quantidade=quantidade
        )

        return redirect('lista_vendas')

    return render(request, 'vendas/criar_venda.html', {
        'produtos': produtos,
        'vendedores': vendedores
    })