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

class admin_cadastro_viagem(admin.ModelAdmin):
    list_display = ('id', 'cadastro','viagem','data_do_inicio','data_do_fim','valor_final')
    list_display_links = ('id','cadastro')
    search_fields = ['cadastro']
    list_per_page = 10

admin.site.register(cadastro_viagem_usuario,admin_cadastro_viagem)