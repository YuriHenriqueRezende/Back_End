from rest_framework import filters
import django_filters

from .models import *


class InvoiceFilter(django_filters.FilterSet):
   code = django_filters.CharFilter(lookup_expr='icontains')
   customerCNPJ = django_filters.CharFilter(lookup_expr='icontains')
   emissionDate = django_filters.DateFromToRangeFilter()

   class Meta:
      model = Invoice
      fields = ['code','customerCNPJ','emissionDate']

class InvoiceItemFilter(django_filters.FilterSet):
   invoiceFK = django_filters.CharFilter(lookup_expr='exact')
   productFK = django_filters.CharFilter(lookup_expr='exact')

   class Meta:
      model = InvoiceItem
      fields = ['invoiceFK','productFK']


class WarrantyFilter(django_filters.FilterSet):
   status = django_filters.CharFilter(lookup_expr='icontains')

   class Meta:
      model = Warranty
      fields = ['status']