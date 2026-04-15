from django.db import models
from django.core.exceptions import ValidationError


class Produto(models.Model):
    nome = models.CharField(max_length=100)
    marca = models.CharField(max_length=50)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade_estoque = models.IntegerField()

    def __str__(self):
        return self.nome
    
class Vendedor(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
       return self.nome


class Venda(models.Model):
    produto = models.ForeignKey('Produto', on_delete=models.CASCADE)
    vendedor = models.ForeignKey('Vendedor', on_delete=models.CASCADE)
    quantidade = models.IntegerField()
    valor_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)
    data_venda = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Venda {self.id}"

    def clean(self):
        if not self.produto:
            raise ValidationError("Produto é obrigatório")

        if self.quantidade <= 0:
            raise ValidationError("Quantidade inválida")
        
def save(self, *args, **kwargs):
    print("ESTOQUE:", self.produto.quantidade_estoque)
    print("QUANTIDADE:", self.quantidade)


    self.valor_unitario = self.produto.preco

 
    if self.quantidade > self.produto.quantidade_estoque:
        raise ValueError("Estoque insuficiente")

    self.valor_total = self.quantidade * self.valor_unitario

    if not self.pk:
        self.produto.quantidade_estoque -= self.quantidade
        self.produto.save()

    
    super().save(*args, **kwargs)        
