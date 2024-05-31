from rest_framework import serializers
from .models import *


class UsuarioCustomizadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsuarioCustomizado
        fields = ['id','email','telefone','cpf','endereco','is_active','groups','user_permissions']
        many = True

class CategoriaProdutosSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriaProdutos
        fields = '__all__'
        many = True

class FotoSerializer(serializers.ModelSerializer):
    class Meta:
        models = Foto
        fields = '__all__'
        many = True

class ProdutosSerializer(serializers.ModelSerializer):
    #fotos = FotoSerializer(read_only=True) #fazer o join com tabelas separadas
    fotos = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='url'
    ) #join com many to many field
    categoriaFK = CategoriaProdutosSerializer(read_only=True)
    class Meta:
        model = Produtos
        fields = '__all__'
        many = True


class VendasSerializer(serializers.ModelSerializer):
    #usuarioFK = UsuarioCustomizadoSerializer(read_only=True)
    class Meta:
        model = Vendas
        fields = '__all__'
        many = True


class VendaProdutosSerializer(serializers.ModelSerializer):
    produtoFK = ProdutosSerializer

    class Meta:
        many = True
        model = VendasProdutos
        fields = '__all__'

