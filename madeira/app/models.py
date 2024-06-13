from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .gerenciador import Gerenciador
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Usuario(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField("endereço de email", unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    telefone = models.CharField(max_length=15, null=True, blank=True)
    cpf = models.CharField(max_length=20)

    objects = Gerenciador()
    REQUIRED_FIELDS = []

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

CATEGORIAS = [
    ("SALA DE ESTAR"),
    ("ESCRITORIO"),
    ("SALA DE JANTAR"),
    ("INFANTIL"),
]

FORMA_PAGAMENTOS = [
    ("P", "PIX"),
    ("D", "DEBITO"),
    ("C","CREDITO"),
    ("B", "BOLETO"),
    ("V","VALE PRESENTE"),
]

STATUS = [
        ("P","Pendente"),
        ("C","Cancelado(a)"),
        ("A","Aprovado(a)")
]

class pecas(models.Model):
    nome = models.CharField(max_length=20)
    imagem = models.CharField(max_length=200)
    medida = models.IntegerField()
    peso = models.IntegerField()
    valor = models.DecimalField(max_digits=10,decimal_places=2)
    descricao = models.CharField(max_length=200)
    parcelamento = models.CharField(max_length=20)

    def __str__(self):
        return self.nome


class produto(models.Model):
    nome = models.CharField(max_length=20)
    imagem = models.CharField(max_length=200)
    peso = models.IntegerField()
    medida = models.IntegerField()
    valor = models.DecimalField(max_digits=10,decimal_places=2)
    descricao = models.CharField(max_length=200)
    score = models.IntegerField(null=True, blank=True, validators=[MinValueValidator(0), MaxValueValidator(10)])
    parcelamento = models.CharField(max_length=20)
    subprodutoFK = models.ManyToManyField(pecas)

    def __str__(self):
        return self.nome

    def subproduto(self):
        return ",".join([str(p) for p in self.subprodutoFK.all()])
    


class carrinho(models.Model):
    produtoFK = models.ManyToManyField(produto)
    valor_final = models.DecimalField(max_digits=10,decimal_places=2)

    def __str__(self):
        return self.valor_final
    
    def produto_carrinho(self):
        return ",".join([str(p) for p in self.produtoFK.all()])

class pagamento(models.Model):
    valor_carrinho = models.ForeignKey(carrinho, related_name='carrinhoFKFK', on_delete=models.CASCADE)
    frete = models.IntegerField()
    forma_pagamento = models.CharField(max_length=100, choices=FORMA_PAGAMENTOS)
    cupom = models.IntegerField()
    valor_total = models.DecimalField(max_digits=10,decimal_places=2)
    status = models.CharField(max_length=100, choices=STATUS, default="P")

    def __str__(self):
        return self.valor_total

class pedidos(models.Model):
    status = models.ForeignKey(pagamento, related_name='pagamentoFKFK', on_delete=models.CASCADE)

    def __str__(self):
        return self.status


class imagem(models.Model):
    titulo = models.CharField(max_length=20)
    link = models.CharField(max_length=200)
    produtoFK = models.ForeignKey(produto, related_name='imagemFKFK', on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo