import datetime
from django.contrib.auth.models import User
from django.db import models


# Create your models here.
# Temos que trocar o DatetimeField por 2 datefield e 2 timefield. Pois o DatetimeField
# permite que deixe um dos campos em branco, mesmo utilizando o (blank = True).

class Usuario(models.Model):
    usuario = models.ForeignKey(User, related_name="Usuario", on_delete=models.CASCADE)
    nome = models.CharField(max_length=60, null=False)
    email = models.EmailField(max_length=45, null=False)
    bio = models.TextField(blank=True)
    telefone = models.CharField(max_length=12, null=True, blank=True)

    foto_de_Perfil = models.ImageField(upload_to='perfil', null=True, blank=True)

    def __str__(self):
        return self.nome


class Instituicao(Usuario):
    tipo = 'Instituição'
    endereco = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Instituições"

class Pessoa(Usuario):
    tipo='Pessoa'
    dataNascimento = models.DateField(null=True, verbose_name='Data de Nascimento', blank=True)

    class Meta:
        verbose_name_plural = "Pessoas"

class Compromisso(models.Model):
    titulo = models.CharField(max_length=60, null=False)
    discricao = models.TextField(blank=True)
    local = models.CharField(max_length=100, null=True, blank=True)
    dataInicio = models.DateField(null=True, verbose_name='Data de Inicio',blank=True)
    horaInicio = models.TimeField(null=True, verbose_name='Hora de Inicio', blank=True)
    dataFim = models.DateField(null=True, verbose_name='Data de Termino', blank=True)
    horaFim = models.TimeField(null=True, verbose_name='Hora de Termino', blank=True)
    dataCriacao = datetime.datetime.now()  # armazena a data em que este Compromisso foi criado
    foto = models.ImageField(upload_to='compromissoFoto', null=True, blank=True)

    class Meta:
        verbose_name_plural = "Compromissos"

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

    class Meta:
        verbose_name_plural = "Compromissos Pessoais"

class Tarefas(models.Model):
    nometarefa = models.CharField(max_length=20, null=False, verbose_name="tarefa")
    dataCriacao = datetime.datetime.now()

    class Meta:
        verbose_name_plural = "Tarefas"

    def __str__(self):
        return self.nometarefa


class CompromissoInstitucional(Compromisso):
    compromisso = models.ForeignKey(Tarefas, max_length=20, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Compromisso Institucional"

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

    class Meta:
        verbose_name_plural = "Agenda Privada"

class AgendaInstitucional(Agenda):
    tipo = "Agenda Institucional"
    instituicao = models.ForeignKey(Instituicao, on_delete=models.CASCADE, verbose_name='Instituição')
    seguem = models.ManyToManyField(User, blank=True)
    compromissoInstitucional = models.ManyToManyField(CompromissoInstitucional, blank=True,verbose_name='Compromisso Institucional')

    class Meta:
        verbose_name_plural = "Agenda Institucional"

class AgendaPublica(Agenda):
    tipo = "Agenda Publica"
    dono = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    seguem = models.ManyToManyField(User, blank=True)
    compromissoPessoal = models.ManyToManyField(CompromissoPessoal, blank=True, verbose_name='Compromissos')

    class Meta:
        verbose_name_plural = "Agenda Publica"
# Cada Caminho das imagens segue para uma pasta especifica
