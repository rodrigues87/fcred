from django.shortcuts import render, redirect


def index(request):
    if request.user.is_authenticated:
        return redirect('indicacoes/minhas_indicacoes/')
    else:
        return redirect('/usuarios/login')