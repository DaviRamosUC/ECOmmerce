from django.urls import path
from ECOmmerce.views import HomeView, CadastroView, solicitacadastro

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('solicitacadastro', solicitacadastro, name='solicitacadastro'),
    path('cadastro', CadastroView, name='cadastro')
]
