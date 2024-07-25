from rest_framework import filters
import django_filters
from .models import *

class CategoryUsuario(django_filters.FilterSet):
    nome = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = usuario
        fields = ['nome']


class CategoryLogistica(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    marca = django_filters.CharFilter(lookup_expr='icontains')
    quantidade = django_filters.CharFilter(lookup_expr='lte')
    
    class Meta:
        model = logistica_loja
        fields = ['nome','marca']

class CategoryAutomovel(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    marca = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = categoria_automovel
        fields = ['modelo','marca']