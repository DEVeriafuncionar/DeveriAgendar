from django.shortcuts import render, redirect
from .models import *
from .forms import *


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

def lista_pessoa(request):  # metado de teste pego do SGE
    lista_tipos = Usuario.objects.all()
    return render(request, 'tipo.html', context={'tipos': lista_tipos})


def create_pessoa(request):  # metado de teste pego do SGE
    return render(request, 'pessoa_form.html', context=None)


# esse metado cria o usuario apartir de um formulario completo, ele não está completo e está apresentando erro.
# a cricação do usuario em si está funcionando, o erro está na criação do "Perfil"
# metados de teste pego do SGE.
# @transaction.atomic
def salvar_pessoa(request):  # primeira forma utilizando chave estrangeira

    login = request.POST.get('login')
    senha = request.POST.get('senha')
    if login and senha:
        user = User()
        user.username = login
        user.password = senha
        user.save()  # aqui voce cria o usuario

        usuario2 = Usuario()  # Aqui voce instancia a class usuario
        usuario2.usuario = user  # class Usuario recebe a class User do django
        usuario2.save()  # salva a class Usuario
        nome = request.POST.get('nome')
        email = request.POST.get('email')

        if nome and email:
            p = Pessoa()  # Inicia a class Pessoa
            usuario2.nome = nome  # Como atributo de nome estão na class Usuario quem recebe os atributos de nome e email e ela quem recebe
            usuario2.email = email
            usuario2.save()  # aqui voce cria a class
            p.pessoa = usuario2
            p.save()

    return redirect('/pessoa')


# def salvar_pessoa(request):  # Utilizando segunda forma utilizando Herança
#
#     login = request.POST.get('login')
#     senha = request.POST.get('senha')
#     if login and senha:
#         user = User()
#         user.username = login
#         user.password = senha
#         user.save()
#         nome = request.POST.get('nome')
#         email = request.POST.get('email')
#         if nome and email:
#             p=Pessoa()
#             p.usuario = user
#             p.nome = nome
#             p.email = email
#             p.save()
#
#     return redirect('/pessoa')
#
def show_calendar(request):
    evento = CompromissoPessoal.objects.all()
    return render(request, 'calendar.html', context={'evento': evento})


def agendas_publicas(request):
    lista_agendas = AgendaPublica.objects.all()
    return render(request, 'agenda_publica.html', context={'nome': lista_agendas})


# @login_required
def agendas_privadas(request):
    agendas = AgendaPrivada.objects.all()

    return render(request, 'agenda_privada.html', context={'agenda_privada': agendas})


def create_compromissoPessoal(request):
    titulo = request.POST.get(' tituloEvent ')
    descricao = request.POST.get(' descricaoEvent ')
    local = request.POST.get(' localEvent ')
    dt_inicio = request.POST.get(' dtBeginEvent ')
    hr_inicio = request.POST.get(' hourBeginEvent ')
    dt_fim = request.POST.get(' dtEndEvent ')
    hr_fim = request.POST.get(' hourEndEvent ')
    foto = request.POST.get(' InputFile ')

    evento = CompromissoPessoal.objects.all()
    form = CompromissoPessoalForm(request.POST or None)

    if titulo:
        evento.titulo = titulo

        if descricao:
            evento.discricao = descricao

        if local:
            evento.local = local

        if dt_inicio:
            evento.dataInicio = dt_inicio

        if hr_inicio:
            evento.horaInicio = hr_inicio

        if dt_fim:
            evento.dataFim = dt_fim

        if hr_fim:
            evento.horaFim = hr_fim

        if foto:
            evento.foto = foto

        evento.save()

        return render(request, 'calendar.html', context={'evento': evento,'form':form})
    else:
        return redirect('/calendario/')
