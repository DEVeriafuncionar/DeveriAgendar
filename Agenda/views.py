from django.shortcuts import render, redirect
from .models import *

# Create your views here.

# Desse jeito sera os outros forms. Os de Criar usuario não será desse jeito por outros motivos que depois qualquer duvida explico.

# class InstituicaoForm(ModelForm):
#     class Meta:
#         model = Instituicao
#         fields = ['usuario', 'nome', 'email', 'bio', 'telefone', 'foto_de_Perfil',
#               'endereco']
#
# class PessoaForm(ModelForm):
#     class Meta:
#         model = Instituicao
#         fields = ['usuario', 'nome', 'email', 'bio', 'telefone', 'foto_de_Perfil']
#
# def Cadastrar_Instituicao(request):
#     form = InstituicaoForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         return redirect('instituicao_list')
#     return render(request, 'instituicao_form.html',{'form':form})
#
# def Cadastrar_Pessoa(request):
#     form = PessoaForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         return redirect('pessoa_list')
#     return render(request, 'pessoa_form.html',{'form':form})


def lista_pessoa(request): #metado de teste pego do SGE
    lista_tipos = Pessoa.objects.all()
    return render(request, 'tipo.html', context={'tipos':lista_tipos})

def create_pessoa(request): #metado de teste pego do SGE
    return render(request, 'pessoa_form.html', context=None)

#esse metado cria o usuario apartir de um formulario completo, ele não está completo e está apresentando erro.
#a cricação do usuario em si está funcionando, o erro está na criação do "Perfil"
def salvar_pessoa(request): #metado de teste pego do SGE

    login = request.POST.get('login')
    senha = request.POST.get('senha')
    if login and senha:
        usuario = User()
        usuario.username = login
        usuario.password = senha

        nome = request.POST.get('nome')
        email = request.POST.get('email')
        if nome and email:
            usuario.save()
            p = Pessoa()
            p.nome = nome
            print("print Nome",p.nome)
            p.email = email
            print("Print Email",p.email)
            p.save()

    return redirect('/pessoa')