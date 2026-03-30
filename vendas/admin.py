from django.contrib import admin
from .models import Produto, Venda, Vendedor

admin.site.register(Produto)
admin.site.register(Venda)
admin.site.register(Vendedor)