from django.db import models
from django.utils import timezone

# Create your models here.
class usuario(models.Model):
    nome = models.CharField(max_length=150, null=False)
    CPF = models.IntegerField()

    def __str__(self):
        return self.nome

class registro(models.Model):
    nome_da_maquina = models.CharField(max_length=150, null=False)
    marca = models.CharField(max_length=150, null=False)
    statu = [("Q", "Quebrada"),
              ("P", "Preventiva"),
              ("C", "Corretiva"),
              ("O", "OUTROS"),]
    status = models.CharField(max_length=1, choices=statu, null=False)
    data_do_defeito = models.DateTimeField(auto_now_add=False)
    chamado = models.DateTimeField(auto_now_add=True)
    comentarios = models.CharField(max_length=150, null=False)
    responsavel = models.ForeignKey(usuario, related_name="usuario", on_delete=models.CASCADE)

    def __str__(self):
        return self.nome_da_maquina
