from django.contrib.auth.hashers import make_password
from django.db import models

class Endereco(models.Model):
    id = models.BigAutoField(primary_key=True)
    logradouro = models.CharField(max_length=120, help_text='Logradouro')
    numero = models.CharField(max_length=10, help_text='Número', null=True)
    complemento = models.CharField(max_length=50, help_text='Complemento', null=True)
    bairro = models.CharField(max_length=80, help_text='Bairro')
    estado =  models.CharField(max_length=20, help_text='Estado')
    cep = models.CharField(max_length=9, help_text='CEP')

    class Meta:
        ordering = ['id']

class Usuario(models.Model):
    TIPO_USUARIO = (
        ('PJ', 'Pessoa Juridica'),
        ('PF', 'Pessoa Fisica')
    )

    id = models.BigAutoField(primary_key=True)
    nomeUsuario = models.CharField(max_length=60, help_text='Nome completo')
    cpf = models.CharField(max_length=11, help_text='CPF - Ex: 1234567891011', unique= True)
    cnpj = models.CharField(max_length=11, help_text='CPF - Ex: 1234567891011', unique= True)
    celular = models.CharField(max_length=12, help_text='Número para contato')
    email = models.EmailField(max_length=20, help_text='Email', unique= True)
    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE)
    tipoUsuario = models.CharField(max_length=2, choices=TIPO_USUARIO)
    senha = models.CharField(max_length=20, help_text='Senha')

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.nomeCompleto + ' - ' + cpf

class Produto(models.Model):
    id = models.BigAutoField(primary_key=True)
    nomeProduto = models.CharField(max_length=50, help_text='Nome do produto')
    preco = models.FloatField()

    class Meta:
        ordering = ['id']


class Categoria(models.Model):
    id = models.BigAutoField(primary_key=True)
    nomeCategoria = models.CharField(max_length=50, help_text='Nome da categoria')
    produtos = models.ManyToManyField(Produto)

    class Meta:
        ordering = ['nomeCategoria']

class Pedido(models.Model):
    id = models.BigAutoField(primary_key=True)
    produtos = models.ManyToOneRel(Produto)
    cliente = models.OneToOneField()
