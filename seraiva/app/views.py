from django.shortcuts import render
from .models import *
from .serializers import *

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class UsuarioView(ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioCustomizadoSerializer

class fotoslivroView(ModelViewSet):
    queryset = fotoslivro.objects.all()
    serializer_class = fotoslivroSerializer

class categoriasView(ModelViewSet):
    queryset = categorias.objects.all()
    serializer_class = categoriasSerializer

class livroView(ModelViewSet):
    queryset = livro.objects.all()
    serializer_class = livroSerializer

class emprestimoView(ModelViewSet):
    queryset = emprestimo.objects.all()
    serializer_class = emprestimoSerializer
