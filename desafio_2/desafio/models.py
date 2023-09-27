from django.db import models
from django.utils import timezone
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
    categoria = models.ForeignKey(categoria, related_name="categoria", on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo
    

class cadastro_viagem_usuario(models.Model):
    cadastro = models.ForeignKey(cadastro, related_name="cadastro", on_delete=models.CASCADE)
    viagem = models.ForeignKey(viagens, related_name="viagens", on_delete=models.CASCADE)
    data_do_inicio = models.DateField(auto_now_add=False)
    data_do_fim = models.DateField(auto_now_add=False)

    
    def __str__(self):
        return self.cadastro



