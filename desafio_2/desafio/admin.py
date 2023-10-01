from django.contrib import admin
from .models import *

# Register your models here.
# Register your models here.
class admin_cadastro(admin.ModelAdmin):
    list_display = ('id', 'nome','CPF','email','cep','telefone')
    list_display_links = ('id','nome')
    search_fields = ['nome']
    list_per_page = 10

admin.site.register(cadastro,admin_cadastro)


class admin_categoria(admin.ModelAdmin):
    list_display = ('id', 'nome')
    list_display_links = ('id','nome')
    search_fields = ['nome']
    list_per_page = 10

admin.site.register(categoria,admin_categoria)


class admin_viagem(admin.ModelAdmin):
    list_display = ('id', 'titulo','imagem','descrição','valor','endereço','cidade','categoria')
    list_display_links = ('id','titulo')
    search_fields = ['titulo']
    list_per_page = 10

admin.site.register(viagens,admin_viagem)

class admin_data(admin.ModelAdmin):
    list_display = ('id','horario_inicio','horario_fim','lugar')
    list_display_links = ('id','lugar')
    search_fields = ['lugar']
    list_per_page = 10

admin.site.register(horario,admin_data)

class admin_pagamento(admin.ModelAdmin):
    list_display = ('id','forma_de_pagamento','status','usuario','valor','registrado')
    list_display_links = ('id','forma_de_pagamento')
    search_fields = ['forma_de_pagamento']
    list_per_page = 10

admin.site.register(pagamento,admin_pagamento)

class admin_reservas(admin.ModelAdmin):
    list_display = ('id','nome','avaliacao')
    list_display_links = ('id','nome')
    search_fields = ['id']
    list_per_page = 10

admin.site.register(reservas,admin_reservas)
