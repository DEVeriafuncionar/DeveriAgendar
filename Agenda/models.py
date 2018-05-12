from django.contrib.auth.models import User
from django.db import models


# Create your models here.


class Pessoa(models.Model):
    Usuario = models.ForeignKey(User, related_name="Usuario", on_delete=models.CASCADE)
    Nome = models.CharField(max_length=60, null=False)
    email = models.EmailField(max_length=45, null=False)
    bio = models.TextField(blank=True)
    telefone = models.CharField(max_length=12, null=True, blank=True)

    foto_de_Perfil = models.ImageField(upload_to='perfil', null=True, blank=True)


    def __str__(self):
        return self.Nome


class Instituicao(Pessoa):
    tipo = 'Instituição'
    endereco = models.CharField(max_length=255, null=True, blank=True)




# Teste de Prioridade por favor de preferencia não apagar está parte ate o final do desenvolvimento do codigo.
#-----------------------------------------------------------------------------------------------------------------#


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
    dataInicio = models.DateTimeField(null=True, verbose_name='Data e Hora de Inicio', blank = True)
    dataFim = models.DateTimeField(null=True, verbose_name='Data e Hora do terminio', blank=True)

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

    compromisso = models.CharField(max_length=20, null=False, choices=COMPROMISSO_CHOICES)


class Tarefas(models.Model):
    nometarefa = models.CharField(max_length=20, null=False,verbose_name="tarefa")


    def __str__(self):
        return self.nometarefa

class CompromissoInstitucional(Compromisso):
    compromisso = models.ForeignKey(Tarefas, max_length=20, on_delete=models.CASCADE)


class Agenda(models.Model):
    foto_de_capa = models.ImageField(upload_to='capa', null=True, blank=True)
    nome = models.CharField(max_length=35, null=False)
    discricao = models.TextField(blank=True)

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

    compromissoInstitucional = models.ManyToManyField(CompromissoInstitucional, blank=True, verbose_name='Compromisso Institucional')



class AgendaPublica(Agenda):
    tipo = "Agenda Publica"
    dono = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    seguem = models.ManyToManyField(User, blank=True)

    compromissoPessoal = models.ManyToManyField(CompromissoPessoal, blank=True,verbose_name='Compromissos')




#Cada Caminho das imagens segue para uma pasta especifica
