from django.shortcuts import render, redirect, get_object_or_404
from .models import Produto, Venda, Vendedor
from  django.db.models import Sum, Count
from django.http import JsonResponse



def home(request):
    return render(request, 'vendas/home.html')

def register(request):
    return render(request, 'vendas/register.html')

def consult(request):
    return render(request, 'vendas/consult.html')

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
        try:
            Produto.objects.create(
                nome=request.POST.get('nome'),
                marca=request.POST.get('marca'),
                preco=float(request.POST.get('preco')),
                quantidade_estoque=int(request.POST.get('quantidade'))
            )
            return redirect('lista_produtos')

        except Exception as e:
            print(e)
            return render(request, 'vendas/criar_produto.html', {
                'erro': str(e)
            })

    return render(request, 'vendas/criar_produto.html')

def editar_produto(request, id):
    produto = get_object_or_404(Produto, id=id)

    if request.method == 'POST':
        try:
            nome = request.POST.get('nome')
            marca = request.POST.get('marca')
            preco = request.POST.get('preco')
            quantidade = request.POST.get('quantidade')

            if not nome or not marca or not preco or not quantidade:
                raise ValueError("Preencha todos os campos")

            produto.nome = nome
            produto.marca = marca
            produto.preco = float(preco)
            produto.quantidade_estoque = int(quantidade)
            produto.save()

            return redirect('lista_produtos')

        except Exception as e:
            print("ERRO AO EDITAR:", e)
            return render(request, 'vendas/editar_produto.html', {
                'produto': produto,
                'erro': str(e)
            })

    return render(request, 'vendas/editar_produto.html', {
        'produto': produto
    })

def deletar_produto(request, id):
    produto = get_object_or_404(Produto, id=id)
    produto.delete()
    return redirect('lista_produtos')



def lista_vendas(request):
    produto = request.GET.get('produto')
    vendedor = request.GET.get('vendedor')

    vendas = Venda.objects.select_related('produto', 'vendedor').all()

    if produto:
        vendas = vendas.filter(produto__nome__icontains=produto)

    if vendedor:
        vendas = vendas.filter(vendedor__nome__icontains=vendedor)

    return render(request, 'vendas/vendas.html', {
        'vendas': vendas
    })



def criar_venda(request):
    produtos = Produto.objects.all()
    vendedores = Vendedor.objects.all()

    if request.method == 'POST':
        try:
            produto_id = request.POST.get('produto')
            vendedor_id = request.POST.get('vendedor')
            quantidade = request.POST.get('quantidade')

            if not produto_id or not vendedor_id or not quantidade:
                raise ValueError("Preencha todos os campos")

            quantidade = int(quantidade)

            produto = get_object_or_404(Produto, id=produto_id)
            vendedor = get_object_or_404(Vendedor, id=vendedor_id)

            if quantidade <= 0:
                raise ValueError("Quantidade inválida")

            if quantidade > produto.quantidade_estoque:
                raise ValueError("Estoque insuficiente")

            valor_unitario = produto.preco
            valor_total = valor_unitario * quantidade


            produto.quantidade_estoque -= quantidade
            produto.save()

            Venda.objects.create(
                produto=produto,
                vendedor=vendedor,
                quantidade=quantidade,
                valor_unitario=valor_unitario,
                valor_total=valor_total
            )

            return redirect('lista_vendas')

        except Exception as e:
            print("ERRO:", e)

            return render(request, 'vendas/criar_venda.html', {
                'produtos': produtos,
                'vendedores': vendedores,
                'erro': str(e)
            })

    return render(request, 'vendas/criar_venda.html', {
        'produtos': produtos,
        'vendedores': vendedores
    })

def editar_venda(request, id):
    venda = get_object_or_404(Venda, id=id)
    produtos = Produto.objects.all()
    vendedores = Vendedor.objects.all()

    if request.method == 'POST':
        try:
            produto_id = request.POST.get('produto')
            vendedor_id = request.POST.get('vendedor')
            quantidade = int(request.POST.get('quantidade'))

            produto_novo = get_object_or_404(Produto, id=produto_id)
            vendedor = get_object_or_404(Vendedor, id=vendedor_id)

            if quantidade <= 0:
                raise ValueError("Quantidade inválida")

           
            produto_antigo = venda.produto
            produto_antigo.quantidade_estoque += venda.quantidade
            produto_antigo.save()

     
            if quantidade > produto_novo.quantidade_estoque:
                raise ValueError("Estoque insuficiente")

            
            produto_novo.quantidade_estoque -= quantidade
            produto_novo.save()

    
            venda.produto = produto_novo
            venda.vendedor = vendedor
            venda.quantidade = quantidade
            venda.valor_unitario = produto_novo.preco
            venda.valor_total = quantidade * produto_novo.preco
            venda.save()

            return redirect('lista_vendas')

        except Exception as e:
            return render(request, 'vendas/editar_venda.html', {
                'venda': venda,
                'produtos': produtos,
                'vendedores': vendedores,
                'erro': str(e)
            })

    return render(request, 'vendas/editar_venda.html', {
        'venda': venda,
        'produtos': produtos,
        'vendedores': vendedores
    })

def dashboard(request):
    return render(request, 'vendas/dashboard.html')



def dados_dashboard(request):
    total_vendas = Venda.objects.count()

    faturamento_total = Venda.objects.aggregate(
        total=Sum('valor_total')
    )['total'] or 0

    vendas_por_produto = list(
        Venda.objects
        .values('produto__nome')
        .annotate(total=Sum('quantidade'))
        .order_by()[:50]
    )

    top_vendedores = list(
    Venda.objects
      .values('vendedor__nome')
      .annotate(total=Count('id'))
      .order_by('-total')[:5]
    )

    top_produtos = list(
    Venda.objects
    .values('produto__nome')
    .annotate(total=Sum('quantidade'))
    .order_by('-total')[:5]
    )

    return JsonResponse({
        'total_vendas': total_vendas,
        'faturamento_total': float(faturamento_total),
        'vendas_por_produto': vendas_por_produto,
        'top_vendedores': top_vendedores,
        'top_produtos' : top_produtos
    })