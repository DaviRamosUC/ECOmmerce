from django.shortcuts import render
from django.views.generic import  TemplateView
from ECOmmerce.models import Usuario

class HomeView(TemplateView):
    template_name = 'Home/index.html'

def cadastro(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        try:
            usuario = Usuario.objects.get(email=email)
        except Usuario.DoesNotExist:
            return render(request,'Home/index.html', {"titulo_mensagem":"O usuário não tem cadastro", "mensagem":"A tentativa de login falhou, este usuário não está registrado na nossa base de dados. Deseja realizar um cadastro?"})
            
    return render(request,'Home/index.html')