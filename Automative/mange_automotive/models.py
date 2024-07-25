'''
Bom tem muitas coisas para eu melhorar no back_end na questao dos models, mas oque eu 
gastei mais tempo pensando foi nas automações, tipo fazer soma, eu nao sei falar para o meu back_end que
nao existe apenas 1 problema no carro e sim varios e com isso somar os valores dos preçoes e a mao de obra
isso eu nao soube aplicar no projeto.
Eu gastei bastante tempo vendo SE meu projeto ESTA funcionando no front do Django mas percebi que tava
perdendo a linha, entao comecei a aplicar json (insonimia).
Sendo sincero essa avaliação eu tentei fazer com os materiais que tinha, o uso da internet foi mais para entender
o funcionamento como as documentacoes e bugs eu sempre procuro pelo Stack Overflow, enfase em ingles. Me recuso a tirar duvidas fora
do horario de aula. 

'''

from django.db import models
from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class usuario(models.Model):
    nome = models.OneToOneField(User,on_delete=models.CASCADE)
    telefone = models.DecimalField(max_digits=11, decimal_places=0)  
    cpf = models.DecimalField(max_digits=10, decimal_places=0)

    def __str__(self):
        return str(self.nome)


class funcionario(models.Model):
    nome = models.OneToOneField(User,on_delete=models.CASCADE)
    cpf = models.DecimalField(max_digits=10, decimal_places=0)
    nif = models.DecimalField(max_digits=10, decimal_places=0)
    email = models.EmailField()
    telefone = models.DecimalField(max_digits=11, decimal_places=0)

    def __str__(self):
        return str(self.nome)    
    
class categoria_servico(models.Model):
    nome = models.CharField(max_length=50)
    valor_obra = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nome
    
class logistica_loja(models.Model):
    nome = models.CharField(max_length=50)
    marca = models.CharField(max_length=50)
    patrimonio = models.DecimalField(max_digits=120, decimal_places=0)
    quantidade = models.DecimalField(max_digits=10, decimal_places=0)
    valor_compra = models.DecimalField(max_digits=10, decimal_places=2)
    valor_venda = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nome
    
class categoria_automovel(models.Model):
    modelo = models.CharField(max_length=50)
    marca = models.CharField(max_length=50)
    ano = models.DecimalField(max_digits=5, decimal_places=0)
    dono = models.ForeignKey(usuario, related_name='usuario', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.modelo
    
class manuntencao(models.Model):
    automovel_fk = models.ForeignKey(categoria_automovel, related_name='categoria_automovel', on_delete=models.CASCADE)
    servico_fk = models.ManyToManyField(categoria_servico)
    logistica_fk = models.ManyToManyField(logistica_loja)
    funcionario_fk = models.ForeignKey(funcionario, related_name='funcionario', on_delete=models.CASCADE)
    mao_obra = models.DecimalField(max_digits=10,decimal_places=2)

    def __str__(self):
        return str(self.automovel_fk)

    def servico(self):
        return ",".join([str(p) for p in self.servico_fk.all()])
    
    def logistica(self):
        return ",".join([str(s) for s in self.logistica_fk.all()])
    
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
    valor_total = models.DecimalField(max_digits=5, decimal_places=2)
    STATU = [
        ("P","Pendente"),
        ("C","Cancelado(a)"),
        ("A","Aprovado(a)")
    ]
    status = models.CharField(max_length=100, choices=STATU)

    
    @property
    def conta(self):
        valor1 = str(self.manuntencao_fk.servico_fk)
        valor2 = str(self.manuntencao_fk.mao_obra)
        valor3 = str(valor1 + valor2)
        valor4 = str(valor3 - self.desconto) # type: ignore
        return self.valor_total + valor4 # type: ignore
    
    def __str__(self):
        return str(self.valor_total)
    
class reserva(models.Model):
    manuntencao_fk = models.ForeignKey(manuntencao, related_name='manu', on_delete=models.CASCADE, blank=True, null=True)
    posto_trabalho_fk = models.ForeignKey(posto_trabalho, related_name='posto_trabalho', on_delete=models.CASCADE)
    dia_reserva = models.DateField()

    def __str__(self):
        return str(self.manuntencao_fk.automovel_fk.dono) # type: ignore

