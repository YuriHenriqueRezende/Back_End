from django.contrib import admin
from .models import *


# Register your models here.
class admin_usuario(admin.ModelAdmin):
    list_display = ('id', 'nome','cpf','telefone')
    list_display_links = ('id','nome')
    search_fields = ['nome']
    list_per_page = 10

admin.site.register(usuario,admin_usuario)

class admin_fucionario(admin.ModelAdmin):
    list_display = ('id', 'nome','cpf','nif','email','telefone')
    list_display_links = ('id','nome')
    search_fields = ['nome']
    list_per_page = 10

admin.site.register(funcionario,admin_fucionario)

class admin_servico(admin.ModelAdmin):
    list_display = ('id', 'nome','valor_obra')
    list_display_links = ('id','nome')
    search_fields = ['nome']
    list_per_page = 10

admin.site.register(categoria_servico,admin_servico)

class admin_logistica(admin.ModelAdmin):
    list_display = ('id', 'nome','marca','patrimonio','quantidade','valor_compra','valor_venda')
    list_display_links = ('id','nome')
    search_fields = ['nome']
    list_per_page = 10

admin.site.register(logistica_loja,admin_logistica)

class admin_automovel(admin.ModelAdmin):
    list_display = ('id','modelo','marca','ano','dono')
    list_display_links = ('id','modelo',)
    search_fields = ['modelo']
    list_per_page = 10

admin.site.register(categoria_automovel,admin_automovel)

class admin_manuntencao(admin.ModelAdmin):
    list_display = ('id','automovel_fk','servico','logistica','funcionario_fk','mao_obra')
    list_display_links = ('id','automovel_fk')
    search_fields = ['automovel_fk']
    list_per_page = 10

admin.site.register(manuntencao,admin_manuntencao)

class admin_posto_trabalho(admin.ModelAdmin):
    list_display = ('id','bloco','funcionario_fk')
    list_display_links = ('id','bloco')
    search_fields = ['bloco']
    list_per_page = 10

admin.site.register(posto_trabalho,admin_posto_trabalho)

class admin_pagamento(admin.ModelAdmin):
    list_display = ('id','manuntencao_fk','desconto','forma_pagamento','dados','valor_total','status')
    list_display_links = ('id','status')
    search_fields = ['status']
    list_per_page = 10

admin.site.register(pagamento,admin_pagamento)

class admin_reserva(admin.ModelAdmin):
    list_display = ('id','manuntencao_fk','posto_trabalho_fk','dia_reserva')
    list_display_links = ('id','dia_reserva')
    search_fields = ['dia_reserva']
    list_per_page = 10

admin.site.register(reserva,admin_reserva)