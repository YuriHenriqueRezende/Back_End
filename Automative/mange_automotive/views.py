from django.shortcuts import render

# Create your views here.from .models import *
from .serializers import *
from rest_framework.views import APIView # Manual #
from rest_framework.viewsets import ModelViewSet # Automatico #
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissionsOrAnonReadOnly 
from .customFilters import * 


class usuarioAPIView(ModelViewSet):
    queryset = usuario.objects.all()
    serializer_class = usuarioSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_class = CategoryUsuario

class funcionarioAPIView(ModelViewSet):
    queryset = funcionario.objects.all()
    serializer_class = funcionarioSerializer
    filter_backends = [DjangoFilterBackend]
    ordering_fields = '__all__'
    permission_classes = (DjangoModelPermissionsOrAnonReadOnly,) 

class categoria_servicoAPIView(ModelViewSet):
    queryset = categoria_servico.objects.all()
    serializer_class = categoria_servicoSerializer
    filter_backends = [DjangoFilterBackend]
    ordering_fields = '__all__'
    permission_classes = (DjangoModelPermissionsOrAnonReadOnly,)

class logistica_lojaAPIView(ModelViewSet):
    queryset = logistica_loja.objects.all()
    serializer_class = logistica_lojaSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_class = CategoryLogistica
    permission_classes = (DjangoModelPermissionsOrAnonReadOnly,)

class categoria_automovelAPIView(ModelViewSet):
    queryset = categoria_automovel.objects.all()
    serializer_class = categoria_automovelSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_class = CategoryAutomovel
    permission_classes = (DjangoModelPermissionsOrAnonReadOnly,)

class manuntencaoAPIView(ModelViewSet):
    queryset = manuntencao.objects.all()
    serializer_class = manuntencaoSerializer
    filter_backends = [DjangoFilterBackend]
    ordering_fields = '__all__'
    permission_classes = (DjangoModelPermissionsOrAnonReadOnly,)

class posto_trabalhoAPIView(ModelViewSet):
    queryset = posto_trabalho.objects.all()
    serializer_class = posto_trabalhoSerializer
    filter_backends = [DjangoFilterBackend]
    ordering_fields = '__all__'
    permission_classes = (DjangoModelPermissionsOrAnonReadOnly,)

class pagamentoAPIView(ModelViewSet):
    queryset = pagamento.objects.all()
    serializer_class = posto_trabalhoSerializer
    filter_backends = [DjangoFilterBackend]
    ordering_fields = '__all__'
    permission_classes = (DjangoModelPermissionsOrAnonReadOnly,)   

class reservaAPIView(ModelViewSet):
    queryset = reserva.objects.all()
    serializer_class = reservaSerializer
    filter_backends = [DjangoFilterBackend]
    ordering_fields = '__all__'
    permission_classes = (DjangoModelPermissionsOrAnonReadOnly,)   
