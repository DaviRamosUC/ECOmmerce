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
        db_table="Endereco"

class Usuario(models.Model):
    
    id = models.BigAutoField(primary_key=True)
    nomeUsuario = models.CharField(max_length=60, help_text='Nome completo')
    cpfOuCnpj = models.CharField(max_length=13, help_text='CPF - Ex: 1234567891011', unique= True)
    celular = models.CharField(max_length=12, help_text='Número para contato')
    email = models.EmailField(max_length=20, help_text='Email', unique= True)
    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE)
    senha = models.CharField(max_length=20, help_text='Senha')
    class Meta:
        ordering = ['id']
        db_table="Usuario"

    def __str__(self):
        return self.nomeCompleto + ' - ' + cpf

class Produto(models.Model):
    id = models.BigAutoField(primary_key=True)
    nomeProduto = models.CharField(max_length=50, help_text='Nome do produto')
    descricao = models.CharField(max_length=300, help_text='Descrição do produto')
    subdescricao = models.CharField(max_length=30, help_text='Subdescrição do produto')
    preco = models.FloatField()
    imagem = models.CharField(max_length=180, help_text='Imagem do produto')

    class Meta:
        ordering = ['id']
        db_table="Produto"


class Categoria(models.Model):
    id = models.BigAutoField(primary_key=True)
    nomeCategoria = models.CharField(max_length=50, help_text='Nome da categoria')
    produtos = models.ManyToManyField(Produto)

    class Meta:
        ordering = ['nomeCategoria']
        db_table="Categoria"

class Pedido(models.Model):
    id = models.BigAutoField(primary_key=True)
    produtos = models.ForeignKey(Produto, on_delete=models.CASCADE, related_name='pedidos')
    cliente = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    class Meta:
        ordering = ['id']
        db_table="Pedido"