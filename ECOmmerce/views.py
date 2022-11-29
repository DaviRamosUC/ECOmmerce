from django.shortcuts import render
from django.views.generic import  TemplateView
from ECOmmerce.models import Usuario, Endereco, Produto
from django.shortcuts import redirect

def HomeView(request):
    produtos = Produto.objects.all()
    return render(request, 'index.html', {'produtos': produtos})

def solicitacadastro(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        try:
            usuario = Usuario.objects.get(email=email)
        except Usuario.DoesNotExist:
            return render(request,'index.html', {"titulo_mensagem":"O usuário não tem cadastro", "mensagem":"A tentativa de login falhou, este usuário não está registrado na nossa base de dados. Deseja realizar um cadastro?"})
            
    return redirect(produtos)

def CadastroView(request):
    return render(request, 'cadastro.html')

def produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'produtos.html', {'produtos': produtos})

def cadastrar(request):
    if request.method == 'POST':
        endereco = Endereco()
        endereco.cep = request.POST['cep']
        endereco.rua = request.POST['rua']
        endereco.numero = request.POST['numero']
        endereco.complemento = request.POST['complemento']
        endereco.bairro = request.POST['bairro']
        endereco.cidade = request.POST['cidade']
        endereco.estado = request.POST['estado']
        endereco.save()

        usuario = Usuario()
        usuario.nomeUsuario = request.POST['first-name']
        usuario.cpf = request.POST['identity-number']
        usuario.celular = request.POST['tel']
        usuario.email = request.POST['email']
        usuario.senha = request.POST['password']
        usuario.endereco = endereco
        usuario.save()
        redirect(produtos)