from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from .manager import *
from django.core.validators import FileExtensionValidator

class CustomUser(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField("email address", unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    registrationNumber = models.CharField(max_length=30)
    phoneNumber = models.CharField(max_length=15, null=True, blank=True)
    is_email_verified = models.BooleanField(default=False)
    name = models.CharField(default='',max_length=100)
    
    USERNAME_FIELD = "email" 
    REQUIRED_FIELDS = []

    objects = CustomManager()

    def __str__(self):
        return self.email    
    
class ProductFiles(models.Model):
    file = models.FileField(upload_to='product_files', validators=[FileExtensionValidator(allowed_extensions=['xlsx'])])
    fileRead = models.BooleanField(default=False)

class ProductCategory(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    categoryFK = models.ForeignKey(ProductCategory, related_name='productCategoryFK', on_delete=models.CASCADE)
    weight = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=300)    
    creationDate = models.DateTimeField(auto_now_add=True)
    barCode = models.CharField(max_length=15)
    image = models.CharField(max_length=1000)
    
    def __str__(self):
        return self.name
    
    

class Invoice(models.Model):
    code = models.CharField(max_length=30)
    customerName = models.CharField(max_length=100)
    customerCNPJ = models.CharField(max_length=20)
    sellerName = models.CharField(max_length=100)
    sellerCNPJ = models.CharField(max_length=20)
    totalValue = models.DecimalField(max_digits=10, decimal_places=2)
    emissionDate = models.DateField()
    uploadDate = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.code

class InvoiceItem(models.Model):
    productFK = models.ForeignKey(Product, related_name='invoiceItemProduct', on_delete=models.CASCADE)
    invoiceFK = models.ForeignKey(Invoice, related_name='invoiceItemInvoice', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return str(self.invoiceFK.id) + '-' + self.productFK.name


WARRANTY_STATUS = [
    ('P','Pendent'),
    ('A','Approved'),
    ('R', 'Refused')
]

class Warranty(models.Model):
    status = models.CharField(max_length=30,choices=WARRANTY_STATUS)
    description = models.CharField(max_length=200, blank=True, null=True)
    creationDate = models.DateTimeField(auto_now_add=True)
    createdByFK = models.ForeignKey(CustomUser, related_name='createdWarrantyUser', on_delete=models.CASCADE)
    approverFK = models.ForeignKey(CustomUser, related_name='approverWarrantyUser', on_delete=models.CASCADE, blank=True, null=True)
    items = models.ManyToManyField(InvoiceItem)

    def __str__(self):
        return self.status

