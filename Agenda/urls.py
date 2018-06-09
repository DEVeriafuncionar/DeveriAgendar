from django.urls import path
from .views import *

urlpatterns =[
    path('agendas/calendario/',show_calendar),
	path('pessoa/', lista_pessoa, name='home_tipos'),
    path('pessoa/add', create_pessoa, name='create_pessoa'),
    path('pessoa/salvar/', salvar_pessoa, name='salvar_pessoa'),

    path('usuario/(<string:username>)/agendas/publicas/',agendas_publicas,name='agendas_publicas'),
    path('usuario/(<string:username>)/agendas/privadas/',agendas_privadas,name='agendas_privadas'),
    path('usuario/(<string:username>)/agendas/institucionais/',agendas_privadas,name='agendas_privadas'),

    path('usuario/(<string:username>)/agendas/publicas/(<int:pk>)/calender',agendas_publicas,name='agendas_publicas'),
    path('usuario/(<string:username>)/agendas/privadas/(<int:pk>)/calender',agendas_privadas,name='agendas_privadas'),
    path('usuario/(<string:username>)/agendas/institucionais/(<int:pk>)/calendar',agendas_privadas,name='agendas_privadas'),
    path('usuario/(<string:username>)/agendas/institucionais/<int:pk>/calendar',agendas_privadas,name='agendas_privadas'),

    path('createEventoPessoal',create_compromissoPessoal)

]
