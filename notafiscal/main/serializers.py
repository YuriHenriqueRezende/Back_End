from rest_framework import serializers
from .models import *
from rest_framework.serializers import ModelSerializer, SlugRelatedField, PrimaryKeyRelatedField, StringRelatedField

class CustomUserSerializer(serializers.ModelSerializer):
    groups = SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name',
    )

    class Meta:
        model = CustomUser
        fields = ('id', 'email', 'groups', 'name', )
        many = True


class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = '__all__'
        many = True

class ProductReadSerializer(serializers.ModelSerializer):
    categoryFK = ProductCategorySerializer()

    class Meta:
        model = Product
        fields = '__all__'
        many = True

class ProductWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        many = True

class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = '__all__'
        many = True

class InvoiceItemReadSerializer(serializers.ModelSerializer):
    productFK = ProductReadSerializer()
    invoiceFK = InvoiceSerializer()

    class Meta:
        model = InvoiceItem
        fields = '__all__'
        many = True

class InvoiceItemWriteSerializer(serializers.ModelSerializer):    
    class Meta:
        model = InvoiceItem
        fields = '__all__'
        many = True

class WarrantyReadSerializer(serializers.ModelSerializer):    
    createdByFK = CustomUserSerializer()
    approverFK = CustomUserSerializer()
    
    class Meta:
        model = Warranty
        fields = '__all__'
        many = True

class WarrantyWriteSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Warranty
        fields = '__all__'
        many = True