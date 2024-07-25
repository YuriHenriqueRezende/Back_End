from rest_framework import serializers
from . models import *

class UsuarioCustomizadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'
        many = True

class pecasSerializer(serializers.ModelSerializer):
    class Meta:
        model = pecas
        fields = '__all__'
        many = True

class produtoSerializer(serializers.ModelSerializer):
    class Meta:
        model = produto
        fields = '__all__'
        many = True

class carrinhoSerializer(serializers.ModelSerializer):
    class Meta:
        model = carrinho
        fields = '__all__'
        many = True

class pagamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = pagamento
        fields = '__all__'
        many = True

class pedidosSerializer(serializers.ModelSerializer):
    class Meta:
        model = pedidos
        fields = '__all__'
        many = True

class imagemSerializer(serializers.ModelSerializer):
    class Meta:
        model = imagem
        fields = '__all__'
        many = True