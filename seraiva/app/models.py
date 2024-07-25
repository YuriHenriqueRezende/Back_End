from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .gerenciador import Gerenciador

# Create your models here.
STATUS = [
        ("P","Pendente"),
        ("C","Cancelado(a)"),
        ("A","Aprovado(a)")
]

FORMATOS = [
        ("E-BOOK","E-BOOK"),
        ("FISICO","FISICO")
]

CARGOS = [
        ("A","ADMIN"),
        ("B","BIBLIOTECARIO(A)"),
        ("AU","AUTOR(A)"),
        ("U","USUARIO(A)"),
]

BIBLIOTECA = [
        ("D","DEVOLVIDO"),
        ("A","ATRASADO"),
        ("E","EMPRESTADO"),

]
    
class Usuario(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField("endereço de email", unique=True)
    nome = models.CharField(max_length=50, null=True, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    cpf = models.CharField(max_length=20, null=True, blank=True)
    biografia = models.TextField(null=True, blank=True)
    foto = models.URLField(max_length=200, verbose_name="Image URL", null=True, blank=True)
    cargo = models.CharField(max_length=100, choices=CARGOS, default="U")

    objects = Gerenciador()
    REQUIRED_FIELDS = []

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

class fotoslivro(models.Model):
    nome = models.CharField(max_length=50, null=True, blank=True)
    link = models.URLField(max_length=200, verbose_name="Image URL")

    def __str__(self):
        return self.nome
    

class categorias(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class livro(models.Model):
    titulo = models.CharField(max_length=50)
    descricao = models.TextField()
    numero_pagina = models.IntegerField()
    formato = models.CharField(max_length=100, choices=FORMATOS)
    numero_edicao = models.IntegerField()
    autor = models.ForeignKey(Usuario, related_name='usuariosFKFK', on_delete=models.CASCADE)
    publicacao = models.IntegerField()
    categoriaFK = models.ForeignKey(categorias, related_name='categoriasFKFK', on_delete=models.CASCADE)
    status = models.CharField(max_length=100, choices=STATUS, default="P")
    preco = models.DecimalField(max_digits=10,decimal_places=2)
    fotosFK = models.ManyToManyField(fotoslivro)
    quantidade = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.titulo

    def fotos(self):
        return ",".join([str(p) for p in self.fotosFK.all()])
    
class emprestimo(models.Model):
    livroFK = models.ManyToManyField(livro)
    usuarioFK = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='emprestimos')
    data_inicio = models.DateField()
    data_fim = models.DateField()
    status = models.CharField(max_length=100, choices=BIBLIOTECA, default="E")

    def __str__(self):
        return str(self.usuarioFK)
    
    def livros(self):
        return ",".join([str(p) for p in self.livro.all()])
