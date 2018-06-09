from django.forms import ModelForm
from .models import *

class CompromissoPessoalForm(ModelForm):
    class Meta():
        model = CompromissoPessoal
        fields = ['titulo','discricao','local','dataInicio','horaInicio','dataFim','horaFim','foto']

class AgendaPublicaForm(ModelForm):
    class Meta():
        model = AgendaPublica
        fields = ['foto_de_capa', 'nome', 'discricao', 'dono', 'seguem', 'compromissoPessoal']

class AgendaPrivadaForm(ModelForm):
    class Meta():
        model = AgendaPrivada
        fields = ['foto_de_capa', 'nome', 'discricao', 'pessoa', 'compromissoPessoal']
