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

def index(request):  #
    return render(request, 'index.html')

def login(request):  #
    return render(request, 'login.html')

def cadastrar(request):  #
    return render(request, 'cadastro.html')


def create_pessoa(request):  # metado de teste pego do SGE
    return render(request, 'pessoa_form.html', context=None)


# esse metado cria o usuario apartir de um formulario completo, ele não está completo e está apresentando erro.
# a cricação do usuario em si está funcionando, o erro está na criação do "Perfil"
# metados de teste pego do SGE.
# @transaction.atomic
def salvar_pessoa(request):
#primeira forma utilizando chave estrangeira

    login = request.POST.get('login')
    senha = request.POST.get('senha')
    if login and senha:
        user = User()
        user.username = login
        user.password = senha
        user.save() # aqui voce cria o usuario

        usuario2 = Usuario() #Aqui voce instancia a class usuario
        usuario2.usuario = user # class Usuario recebe a class User do django
        usuario2.save() # salva a class Usuario
        nome = request.POST.get('nome')
        email = request.POST.get('email')

        if nome and email:
            p = Pessoa() # Inicia a class Pessoa
            usuario2.nome = nome #Como atributo de nome estão na class Usuario quem recebe os atributos de nome e email e ela quem recebe
            usuario2.email = email
            usuario2.save() # aqui voce cria a class
            p.pessoa = usuario2
            p.save()

    return redirect('/index/')

