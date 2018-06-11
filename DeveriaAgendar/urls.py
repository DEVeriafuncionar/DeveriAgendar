"""DeveriaAgendar URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from Agenda.views import *  # Cadastrar_Instituicao,Cadastrar_Pessoa

# assim como as
urlpatterns = [
                  path('', TemplateView.as_view(template_name='home.html'), name='home'),
                  path('admin/', admin.site.urls),
                  path('accounts/', include('Agenda.urls')),
                  path('accounts/', include('django.contrib.auth.urls')),
                  path('contas/', lista_contas, name='home_tipos'),
                  # path('login/', login, name="login"),
                  # path('cadastro/', cadastrar, name="cadastrar"),

                  path('', index, name='index'),
                  path('agendas/calendario/', show_calendar),

                  path('criarconta/', create_conta, name='create_conta'),
                  path('criarconta/salvar/', salvar_conta, name='salvar_conta'),

                  path('agendas/calendario/', show_calendar),
                  path('createagendapublica/', create_agendaPublica, name='create_agendaPublica'),

                  path('usuario/<str:username>/agendas/publicas/', agendas_publicas, name='agendas_publicas'),
                  path('usuario/<str:username>/agendas/privadas/', agendas_privadas, name='agendas_privadas'),
                  # path('usuario/(<string:username>)/agendas/institucionais/', agendas_privadas,  name='agendas_privadas'),

                  #path('usuario/(<string:username>)/agendas/publicas/(<int:pk>)/calender', agendas_publicas, name='agendas_publicas'),
                  #path('usuario/(<string:username>)/agendas/publicas/(<int:pk>)/calender', create_agendaPublica, name='create_agendas_publicas'),
                  #path('usuario/(<string:username>)/agendas/publicas/(<int:pk>)/calender', update_agendaPublica, name='update_agendas_publicas'),
                  #path('usuario/(<string:username>)/agendas/privadas/(<int:pk>)/calender', agendas_privadas, name='agendas_privadas'),
                  #path('usuario/(<string:username>)/agendas/privadas/(<int:pk>)/calender', create_agendaPrivada, name='cria-agendas_privadas'),
                  #path('usuario/(<string:username>)/agendas/privadas/(<int:pk>)/calender', update_agendaPrivada, name='cria-agendas_privadas'),
                  #path('usuario/(<string:username>)/agendas/institucionais/(<int:pk>)/calendar', agendas_institucionais, name='agendas_institucionais'),

                  path('createEventoPessoal/', create_compromissoPessoal),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Essa rota Static e a rota das imagens
