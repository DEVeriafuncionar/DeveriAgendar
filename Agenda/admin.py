from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Pessoa)
admin.site.register(Instituicao)
admin.site.register(Usuario)
admin.site.register(AgendaInstitucional)
admin.site.register(AgendaPrivada)
admin.site.register(AgendaPublica)
admin.site.register(CompromissoPessoal)
admin.site.register(CompromissoInstitucional)
admin.site.register(Tarefas)