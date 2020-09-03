from django.contrib import admin
from django.urls import path
from recomendado.views import *

urlpatterns = [
    path('', list_recomendados, name='list_recomendados'),
    path('create', create_recomendado, name='create_recomendado'),
    path('update/<int:id>', update_recomendado, name='update_recomendado'),
    path('delete/<int:id>', delete_recomendado, name='delete_recomendado'),
]
