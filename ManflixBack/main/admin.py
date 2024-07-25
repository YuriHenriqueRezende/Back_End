from django.contrib import admin
from .models import *

class detAssinatura(admin.ModelAdmin):
    list_display = ('id','nome', 'valor')
    list_display_links = ('id', )
    search_fields = ('nome',)
    list_per_page = 10

admin.site.register(Assinatura, detAssinatura)


class detUsuarios(admin.ModelAdmin):
    list_display = ('id','nome', 'email', 'fone', 'cpf', 'nascimento', 'idUserFK', 'idAssinaturaFK')
    list_display_links = ('id',)
    search_fields = ('nome',)
    list_per_page = 10

admin.site.register(Usuarios, detUsuarios)


class detCategoria(admin.ModelAdmin):
    list_display = ('id','nome')
    list_display_links = ('id', )
    search_fields = ('nome',)
    list_per_page = 10

admin.site.register(Categoria, detCategoria)

class detFilmes(admin.ModelAdmin):
    list_display = ('id','nome', 'foto', 'banner', 'logo', 'descricao', 'idCategoriaFK')
    list_display_links = ('id', )
    search_fields = ('nome',)
    list_per_page = 10

admin.site.register(Filmes, detFilmes)


class detFavorito(admin.ModelAdmin):
    list_display = ('id', 'idUsuarioFK', 'idFilmeFK')
    list_display_links = ('id', )
    list_per_page = 10

admin.site.register(Favoritos, detFavorito)


