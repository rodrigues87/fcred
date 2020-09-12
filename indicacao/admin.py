from django.contrib import admin

from indicacao.models import Indicacao
list_display = ('prospector', 'nome_indicado', 'telefone_indicado','efetivada','data_indicacao','status')
admin.site.register(Indicacao)
