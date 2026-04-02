from django.core.management.base import BaseCommand
from vendas.models import Produto, Vendedor, Venda
import random

class Command(BaseCommand):
    help = 'Gera vendas aleatórias no sistema'

    def add_arguments(self, parser):
        parser.add_argument(
            '--total',
            type=int,
            default=30,
            help='Quantidade de vendas a serem geradas'
        )

    def handle(self, *args, **kwargs):
        total = kwargs['total']

        produtos = list(Produto.objects.all())
        vendedores = list(Vendedor.objects.all())

        if not produtos or not vendedores:
            self.stdout.write(self.style.ERROR(
                'Cadastre produtos e vendedores primeiro!'
            ))
            return

        for _ in range(total):
            produto = random.choice(produtos)
            vendedor = random.choice(vendedores)
            quantidade = random.randint(1, 5)

            valor_unitario = produto.preco
            valor_total = valor_unitario * quantidade

            Venda.objects.create(
                produto=produto,
                vendedor=vendedor,
                quantidade=quantidade,
                valor_unitario=valor_unitario,
                valor_total=valor_total
            )

        self.stdout.write(self.style.SUCCESS(
            f'{total} vendas geradas com sucesso!'
        ))