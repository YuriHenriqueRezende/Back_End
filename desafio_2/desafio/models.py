from django.db import models
from django.utils import timezone
from datetime import timedelta
# Create your models here.


class cadastro(models.Model):
    nome = models.CharField(max_length=150, null=False)
    CPF = models.IntegerField()
    email = models.CharField(max_length=150, null=True)
    cep = models.IntegerField()
    telefone = models.IntegerField()

    def __str__(self):
        return self.nome
    

class categoria(models.Model):
    nome = models.CharField(max_length=150, null=False)

    def __str__(self):
        return self.nome


class viagens(models.Model):
    titulo = models.CharField(max_length=150, null=False)
    imagem = models.CharField(max_length=150, null=True)
    descrição = models.TextField()
    valor = models.IntegerField()
    endereço = models.CharField(max_length=150, null=False)
    cidade = models.CharField(max_length=150, null=False)
    categoria = models.ForeignKey(categoria, related_name="categoria", on_delete=models.CASCADE,blank=True)

    def __str__(self):
        return self.titulo
    
class horario(models.Model):
    horario_inicio = models.DateField(null=True)
    horario_fim = models.DateField(null=True)
    lugar = models.ForeignKey(viagens, related_name="viagens", on_delete=models.CASCADE,null=True,blank=True)
    valor = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return (str(self.lugar))


class pagamento(models.Model):
    statu = [("P", "PIX"), ("D", "DEBITO"), ("C", "CREDITO"), ("B", "BOLETO"),]
    forma_de_pagamento = models.CharField(max_length=1, choices=statu, null=False)

    statuss = [("P", "PENDENTE"), ("A", "APROVADO"), ("R", "RECUSADO")]
    status= models.CharField(max_length=1, choices=statuss, null=False)

    usuario = models.ForeignKey(cadastro, related_name="cadastro", on_delete=models.CASCADE,null=True,blank=True)

    registrado = models.ForeignKey(horario, related_name="horario", on_delete=models.CASCADE,null=True,blank=True)

    valor = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return (str(self.usuario))

class reservas(models.Model):
    nome = models.ForeignKey(pagamento, related_name="pagamento", on_delete=models.CASCADE,null=True,blank=True)
    avaliacao = models.TextField(null=True)

    def __str__(self):
        return (str(self.nome))
