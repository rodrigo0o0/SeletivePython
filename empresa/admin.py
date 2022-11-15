from django.contrib import admin
from .models import Tecnologias, Empresa, Vagas
from vagas.models import Tarefa, Emails



admin.site.register(Tecnologias)
admin.site.register(Empresa)
admin.site.register(Vagas)
admin.site.register(Tarefa)
admin.site.register(Emails)
# Register your models here.
