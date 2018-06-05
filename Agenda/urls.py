from django.urls import path
from .views import *

urlpatterns =[
    path('calendario/',show_calendar),
	path('pessoa/', lista_pessoa, name='home_tipos'),
    path('pessoa/add', create_pessoa, name='create_pessoa'),
    path('pessoa/salvar/', salvar_pessoa, name='salvar_pessoa'),
    path('agendaspublicas/',agendas_publicas,name='agendas_publicas'),
    path('agendasprivadas/',agendas_privadas,name='agendas_privadas'),
    path('createEventoPessoal',create_compromissoPessoal)
]
