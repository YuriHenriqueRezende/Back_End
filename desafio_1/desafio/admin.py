from django.contrib import admin
from .models import *

# Register your models here.
class admin_usuarios(admin.ModelAdmin):
    list_display = ('id', 'nome','CPF')
    list_display_links = ('id','nome')
    search_fields = ['nome']
    list_per_page = 10

admin.site.register(usuario,admin_usuarios)

class admin_registro(admin.ModelAdmin):
    list_display = ('id', 'nome_da_maquina','marca','status','data_do_defeito','chamado','comentarios','responsavel')
    list_display_links = ('id','nome_da_maquina')
    search_fields = ['nome_da_maquina']
    list_per_page = 10

admin.site.register(registro,admin_registro)
