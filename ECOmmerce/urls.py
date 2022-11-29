from django.urls import path
from ECOmmerce.views import HomeView, CadastroView, solicitacadastro, produtos, cadastrar, detalhesProduto

urlpatterns = [
    path('', HomeView, name='home'),
    path('solicitacadastro', solicitacadastro, name='solicitacadastro'),
    path('produtos', produtos, name='produtos'),
    path('cadastro', CadastroView, name='cadastro'),
    path('cadastrar', cadastrar, name='cadastrar'),
    path('detalhes/<str:id>', detalhesProduto, name='detalhes')
]
