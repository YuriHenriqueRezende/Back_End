from django.shortcuts import render

# Create your views here.from .models import *
from .serializers import *
from rest_framework.views import APIView # Manual #
from rest_framework.viewsets import ModelViewSet # Automatico #
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated


class usuarioAPIView(ModelViewSet):
    queryset = usuario.objects.all()
    serializer_class = usuarioSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['nome']

class funcionarioAPIView(ModelViewSet):
    queryset = funcionario.objects.all()
    serializer_class = funcionarioSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['nome']

class categoria_servicoAPIView(ModelViewSet):
    queryset = categoria_servico.objects.all()
    serializer_class = categoria_servicoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['nome']

class logistica_lojaAPIView(ModelViewSet):
    queryset = logistica_loja.objects.all()
    serializer_class = logistica_lojaSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['nome']


class categoria_automovelAPIView(ModelViewSet):
    queryset = categoria_automovel.objects.all()
    serializer_class = categoria_automovelSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['modelo']

class manuntencaoAPIView(ModelViewSet):
    queryset = manuntencao.objects.all()
    serializer_class = manuntencaoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['automovel_fk']

class posto_trabalhoAPIView(ModelViewSet):
    queryset = posto_trabalho.objects.all()
    serializer_class = posto_trabalhoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['bloco']

class pagamentoAPIView(ModelViewSet):
    queryset = pagamento.objects.all()
    serializer_class = posto_trabalhoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['valor_total']

class reservaAPIView(ModelViewSet):
    queryset = reserva.objects.all()
    serializer_class = reservaSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['nome_fk']