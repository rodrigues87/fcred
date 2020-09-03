from django.contrib import admin
from django.urls import path
from dietas.views import *


urlpatterns = [
    path('', list_dietas, name='list_dietas'),
    path('minhas_dietas/', list_minhas_dietas, name='list_minhas_dietas'),
    path('minhas_dietas/submit', submit_dieta, name='submit_dieta'),

    path('create', create_dieta, name='create_dieta'),
    path('update/<int:id>', update_dieta, name='update_dieta'),
    path('delete/<int:id>', delete_dieta, name='delete_dieta'),
    path('add_alimento_dieta/<int:id_alimento>/<int:id_dieta>', add_alimento_dieta, name='add_alimento_dieta')

]
