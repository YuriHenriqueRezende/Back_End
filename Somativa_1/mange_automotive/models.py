from django.db import models
from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

class usuario(models.Model):
    nome = models.CharField(max_length=50)
    cpf = models.DecimalField(max_digits=10, decimal_places=0)
    email = models.EmailField()
    telefone = models.DecimalField(max_digits=11, decimal_places=0)

    def __str__(self):
        return self.nome
    
class funcionario(models.Model):
    nome = models.CharField(max_length=50)
    cpf = models.DecimalField(max_digits=10, decimal_places=0)
    nif = models.DecimalField(max_digits=10, decimal_places=0)
    email = models.EmailField()
    telefone = models.DecimalField(max_digits=11, decimal_places=0)

    def __str__(self):
        return self.nome
    
class categoria_servico(models.Model):
    nome = models.CharField(max_length=50)
    valor_obra = models.DecimalField(max_digits=10, decimal_places=0)

    def __str__(self):
        return self.nome
    
class logistica_loja(models.Model):
    nome = models.CharField(max_length=50)
    marca = models.CharField(max_length=50)
    patrimonio = models.DecimalField(max_digits=120, decimal_places=0)
    quantidade = models.DecimalField(max_digits=10, decimal_places=0)
    valor_compra = models.DecimalField(max_digits=10, decimal_places=0)
    valor_venda = models.DecimalField(max_digits=10, decimal_places=0)

    def __str__(self):
        return self.nome
    
class categoria_automovel(models.Model):
    modelo = models.CharField(max_length=50)
    marca = models.CharField(max_length=50)
    ano = models.DecimalField(max_digits=5, decimal_places=0)

    def __str__(self):
        return self.modelo
    
class manuntencao(models.Model):
    automovel_fk = models.ForeignKey(categoria_automovel, related_name='categoria_automovel', on_delete=models.CASCADE)
    servico_fk = models.ForeignKey(categoria_servico, related_name='categoria_servico', on_delete=models.CASCADE)
    logistica_fk = models.ForeignKey(logistica_loja, related_name='logistica_loja', on_delete=models.CASCADE)
    funcionario_fk = models.ForeignKey(funcionario, related_name='funcionario', on_delete=models.CASCADE)
    mao_obra = models.DecimalField(max_digits=10, decimal_places=0, null=True, blank=True)
    sub_total = models.Count(servico_fk)

    def __str__(self):
        return (str(self.sub_total))

class posto_trabalho(models.Model):
    bloco = models.CharField(max_length=1)
    funcionario_fk = models.ForeignKey(funcionario, related_name='funcionarioo', on_delete=models.CASCADE)

    def __str__(self):
        return self.bloco
    
class pagamento(models.Model):
    manuntencao_fk = models.ForeignKey(manuntencao, related_name='manuntencao', on_delete=models.CASCADE)
    desconto = models.DecimalField(max_digits=5, decimal_places=0)
    formas = [
        ("PIX","PIX"),
        ("B","BOLETO"),
        ("CC","CARTAO DE CREDITO"),
        ("CD","DEBITO"),
    ]
    forma_pagamento = models.CharField(max_length=100, choices=formas)
    dados = models.TextField()
    valor_total = models.DecimalField(max_digits=5, decimal_places=0)
    STATU = [
        ("P","Pendente"),
        ("C","Cancelado(a)"),
        ("A","Aprovado(a)")
    ]
    status = models.CharField(max_length=100, choices=STATU)

    def __str__(self):
        return self.status

class reserva(models.Model):
    nome_fk = models.ForeignKey(usuario, related_name='usuario', on_delete=models.CASCADE)
    posto_trabalho_fk = models.ForeignKey(posto_trabalho, related_name='posto_trabalho', on_delete=models.CASCADE)
    funcionario_fk = models.ForeignKey(funcionario, related_name='funcionarios', on_delete=models.CASCADE)
    dia_reserva = models.DateField()

    def __str__(self):
        return (str(self.lugar))



    


