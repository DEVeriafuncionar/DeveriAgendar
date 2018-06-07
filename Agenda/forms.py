from django.forms import ModelForm
from .models import *

class CompromissoPessoalForm(ModelForm):
    class Meta():
        model = CompromissoPessoal
        fields = ['titulo','discricao','local','dataInicio','horaInicio','dataFim','horaFim','foto']
