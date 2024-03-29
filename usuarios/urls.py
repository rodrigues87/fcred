from django.contrib import admin
from django.urls import path
from usuarios.views import *

urlpatterns = [
    path('', list_usuarios, name='list_usuarios'),
    path('create', create_usuario, name='create_usuario'),
    path('update/<int:id>', update_usuario, name='update_usuario'),
    path('delete/<int:id>', delete_usuario, name='delete_usuario'),
    path('login/', login_user,name='login_user'),
    path('login/submit', submit_login,name='submit_login'),
    path('login/submit_login_google', submit_login_google,name='submit_login_google'),
    path('login/verificar', login_verificar,name='login_verificar'),
    path('login/verificar/submit', login_verificar,name='login_verificar'),
    path('register_prospector', register_prospector, name='register_prospector'),
    path('logout/', logout),

]
