from django.shortcuts import render
from .models import *
from .serializers import *

from rest_framework.viewsets import ModelViewSet

# Create your views here.
class UsuarioView(ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioCustomizadoSerializer

class pecasView(ModelViewSet):
    queryset = pecas.objects.all()
    serializer_class = UsuarioCustomizadoSerializer

class produtoView(ModelViewSet):
    queryset = produto.objects.all()
    serializer_class = produtoSerializer

class carrinhoView(ModelViewSet):
    queryset = carrinho.objects.all()
    serializer_class = carrinhoSerializer

class pagamentoView(ModelViewSet):
    queryset = pagamento.objects.all()
    serializer_class = pagamentoSerializer

class pedidosView(ModelViewSet):
    queryset = pedidos.objects.all()
    serializer_class = pedidosSerializer

class imagemView(ModelViewSet):
    queryset = imagem.objects.all()
    serializer_class = imagemSerializer