import datetime
from django.contrib.auth.models import User
from django.db import models


# Create your models here.
# Temos que trocar o DatetimeField por 2 datefield e 2 timefield. Pois o DatetimeField
# permite que deixe um dos campos em branco, mesmo utilizando o (blank = True).

class Pessoa(models.Model):
    usuario = models.ForeignKey(User, related_name="usuario", on_delete=models.CASCADE)
    nome = models.CharField(max_length=60, null=False)
    email = models.EmailField(max_length=45, null=False)
    bio = models.TextField(blank=True)
    telefone = models.CharField(max_length=12, null=True, blank=True)

    foto_de_Perfil = models.ImageField(upload_to='perfil', null=True, blank=True)

    def __str__(self):
        return self.nome


class Instituicao(Pessoa):
    tipo = 'Instituição'
    endereco = models.CharField(max_length=255, null=True, blank=True)

# Teste de Prioridade por favor de preferencia não apagar está parte ate o final do desenvolvimento do codigo.
# -----------------------------------------------------------------------------------------------------------------#


# class Agenda(models.Model):
#     foto_de_capa = models.ImageField(upload_to='capa', null=True, blank=True)
#     nome = models.CharField(max_length=35, null=False)
#     discricao = models.TextField()
#
#     def __str__(self):
#         return self.nome
#
#
# class AgendaPrivada(Agenda):
#     tipo = "Agenda Privada"
#
#     pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
#
#     compromissoPessoal = models.ManyToManyField(CompromissoPessoal,blank=True)
#     def __str__(self):
#         return self.tipo
#
#
# class AgendaInstituicional(Agenda):
#     tipo = "Agenda Institucional"
#
#     instituicao = models.ForeignKey(Instituicao, on_delete=models.CASCADE)
#
#     seguem = models.ManyToManyField(User, blank=True)
#
#     def __str__(self):
#         return self.tipo
#
#
# class AgendaPublica(Agenda):
#     tipo = "Agenda Publica"
#     dono = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
#     seguem = models.ManyToManyField(User, blank=True)
#
#     def __str__(self):
#         return self.tipo

class Compromisso(models.Model):
    titulo = models.CharField(max_length=60, null=False)
    discricao = models.TextField(blank=True)
    local = models.CharField(max_length=100, null=True, blank=True)
    dataInicio = models.DateTimeField(null=True, verbose_name='Data e Hora de Inicio',blank=True)  # date time puxando como default o dia e hora atual;
    dataFim = models.DateTimeField(null=True, verbose_name='Data e Hora do terminio', blank=True)
    dataCriacao = datetime.datetime.now()  # armazena a data em que este Compromisso foi criado
    foto = models.ImageField(upload_to='compromissoFoto', null=True, blank=True)

    def __str__(self):
        return self.titulo


class CompromissoPessoal(Compromisso):
    COMPROMISSO_CHOICES = (
        ("aniversario", "Aniversário"),
        ("evento", "Evento"),
        ("lembrete", "Lembrete"),
        ("meta", "Meta"),
        ("outro", "Outro")
    )

    compromisso = models.CharField(max_length=20, null=False, choices=COMPROMISSO_CHOICES, help_text='Tipos de eventos que podem vir a ser criado nesta versão da agenda')


class Tarefas(models.Model):
    nometarefa = models.CharField(max_length=20, null=False, verbose_name="tarefa")
    dataCriacao = datetime.datetime.now()

    def __str__(self):
        return self.nometarefa


class CompromissoInstitucional(Compromisso):
    compromisso = models.ForeignKey(Tarefas, max_length=20, on_delete=models.CASCADE)


class Agenda(models.Model):
    foto_de_capa = models.ImageField(upload_to='capa', null=True, blank=True)
    nome = models.CharField(max_length=35, null=False)
    discricao = models.TextField(blank=True)
    dataCriacao = datetime.datetime.now()

    def __str__(self):
        return self.nome


class AgendaPrivada(Agenda):
    tipo = "Agenda Privada"

    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)

    compromissoPessoal = models.ManyToManyField(CompromissoPessoal, blank=True, verbose_name='Compromissos')


class AgendaInstitucional(Agenda):
    tipo = "Agenda Institucional"
    instituicao = models.ForeignKey(Instituicao, on_delete=models.CASCADE, verbose_name='Instituição')
    seguem = models.ManyToManyField(User, blank=True)
    compromissoInstitucional = models.ManyToManyField(CompromissoInstitucional, blank=True,verbose_name='Compromisso Institucional')


class AgendaPublica(Agenda):
    tipo = "Agenda Publica"
    dono = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    seguem = models.ManyToManyField(User, blank=True)
    compromissoPessoal = models.ManyToManyField(CompromissoPessoal, blank=True, verbose_name='Compromissos')

# Cada Caminho das imagens segue para uma pasta especifica
