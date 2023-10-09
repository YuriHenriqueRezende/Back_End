from rest_framework import serializers
from .models import *


class usuarioSerializer(serializers.ModelSerializer):
    class Meta:
        many = True
        model = usuario
        fields = '__all__'


class funcionarioSerializer(serializers.ModelSerializer):
    class Meta:
        many = True
        model = funcionario
        fields = '__all__'


class categoria_servicoSerializer(serializers.ModelSerializer):
    class Meta:
        many = True
        model = categoria_servico
        fields = '__all__'


class logistica_lojaSerializer(serializers.ModelSerializer):
    class Meta:
        many = True
        model = logistica_loja
        fields = '__all__'


class categoria_automovelSerializer(serializers.ModelSerializer):
    class Meta:
        many = True
        model = categoria_automovel
        fields = '__all__'



class manuntencaoSerializer(serializers.ModelSerializer):
    class Meta:
        many = True
        model = manuntencao
        fields = '__all__'


class posto_trabalhoSerializer(serializers.ModelSerializer):
    class Meta:
        many = True
        model = posto_trabalho
        fields = '__all__'


class pagamentoSerializer(serializers.ModelSerializer):
    class Meta:
        many = True
        model = pagamento
        fields = '__all__'


class reservaSerializer(serializers.ModelSerializer):
    class Meta:
        many = True
        model = reserva
        fields = '__all__'

