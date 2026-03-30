from django.test import TestCase

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    categoria = models.CharField(max_length=50)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade_estoque = models.IntegerField()

    def __str__(self):
        return self.nome
    
class Vendedor(models.Model):
    nome = CHarField(max_length=100)

    def __str__(self):
       return self.nome
