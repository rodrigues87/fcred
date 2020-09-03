from django.contrib import admin
from django.urls import path
from fcred.views import *

urlpatterns = [
    path('', list_alimentos, name='list_alimentos'),
    path('create', create_alimento, name='create_alimento'),
    path('update/<int:id>', update_alimento, name='update_alimento'),
    path('delete/<int:id>', delete_alimento, name='delete_alimento'),
]
