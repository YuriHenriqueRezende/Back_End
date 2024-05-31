from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin


# Register your models here.
class AdminUsuarioCustomizado(UserAdmin):
    model=Usuario
    list_display = ['id', 'email',]
    list_display_links = ('id', 'email',)
    ordering = ['email']
    search_fields = ['nome',]

admin.site.register(Usuario,AdminUsuarioCustomizado)

class Adminpecas(admin.ModelAdmin):
    list_display = ['id', 'nome','imagem','medida','peso','valor','descricao','parcelamento']
    list_display_links = ('id', 'nome','imagem','medida','peso','valor','descricao','parcelamento')
    search_fields = ('nome',)
    list_per_page = 10

admin.site.register(pecas,Adminpecas)

class Adminproduto(admin.ModelAdmin):
    list_display = ['id', 'nome','imagem','peso','medida','valor','descricao','score','parcelamento','subproduto']
    list_display_links = ('id', 'nome','imagem','peso','medida','valor','descricao','score','parcelamento','subproduto')
    search_fields = ('nome',)
    list_per_page = 10

admin.site.register(produto,Adminproduto)

class Admincarrinho(admin.ModelAdmin):
    list_display = ['id', 'produto_carrinho','valor_final']
    list_display_links = ('id', 'produto_carrinho','valor_final')
    search_fields = ('produto_carrinho',)
    list_per_page = 10

admin.site.register(carrinho,Admincarrinho)

class Adminpagamento(admin.ModelAdmin):
    list_display = ['id', 'valor_carrinho','frete','forma_pagamento','cupom','valor_total','status']
    list_display_links = ('id', 'valor_carrinho','frete','forma_pagamento','cupom','valor_total','status')
    search_fields = ('valor_carrinho',)
    list_per_page = 10

admin.site.register(pagamento,Adminpagamento)

class Adminpedidos(admin.ModelAdmin):
    list_display = ['id', 'status']
    list_display_links = ('id', 'status')
    search_fields = ('status',)
    list_per_page = 10

admin.site.register(pedidos,Adminpedidos)

class Adminimagem(admin.ModelAdmin):
    link = models.CharField(max_length=200)
    list_display = ['id', 'titulo','link','produtoFK']
    list_display_links = ('id', 'titulo','link','produtoFK')
    search_fields = ('titulo',)
    list_per_page = 10

admin.site.register(imagem,Adminimagem)