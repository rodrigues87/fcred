from django.contrib import admin
from django.urls import path
from indicacao.views import *


urlpatterns = [
    path('', list_indicacoes, name='list_indicacoes'),
    path('minhas_indicacoes/', list_minhas_indicacoes, name='list_minhas_indicacoes'),
    path('minhas_indicacoes/submit', submit_indicacao, name='submit_indicaco'),

    path('create', create_indicacao, name='create_indicaco'),
    path('update/<int:id>', update_indicacao, name='update_indicaco'),
    path('delete/<int:id>', delete_indicacao, name='delete_indicaco'),
    path('add_alimento_indicaco/<int:id_alimento>/<int:id_indicaco>', add_alimento_indicacao, name='add_alimento_indicaco'),
    path('remove_alimento_indicaco/<int:id_alimento>/<int:id_indicaco>', remove_alimento_indicacao, name='remove_alimento_indicaco'),

]
