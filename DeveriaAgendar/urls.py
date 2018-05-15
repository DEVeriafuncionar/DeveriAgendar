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
from django.urls import path

from Agenda.views import *  # Cadastrar_Instituicao,Cadastrar_Pessoa

# assim como as views esses path s�o para teste de cria��o pessoa.
urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('pessoa/', lista_pessoa, name='home_tipos'),
                  path('pessoa/add', create_pessoa, name='create_pessoa'),
                  path('pessoa/salvar', salvar_pessoa, name='salvar_pessoa'),
                  # path('usuario/',lista_usuario,name='lista_usuario'),
                  # path('instituicao/', Cadastrar_Instituicao, name='Cadastrar_Instituicao'),
                  # path('pessoa/', Cadastrar_Pessoa, name='Cadastrar_Pessoa'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Essa rota Static e a rota das imagens
