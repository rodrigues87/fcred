from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect

from django.core import serializers
import json

from indicacao.forms import IndicacaoForm
from indicacao.models import Indicacao
from usuarios.models import Prospector
from django.contrib import messages


def list_minhas_indicacoes(request):
    if request.user.is_authenticated:
        try:
            prospector = Prospector.objects.get(usuario=request.user)
            indicacoes = Indicacao.objects.filter(prospector=prospector)
            return render(request, 'indicacoes/indicacoes_lista.html', {'indicacoes': indicacoes})
        except Prospector.DoesNotExist:
            messages.error(request, "O usuário logado não é um Prospector")

    return redirect('/usuarios/login')


def list_indicacoes(request):
    if request.user.is_authenticated:
        prospector = Prospector.objects.get(usuario=request.user)
        indicacoes = Indicacao.objects.filter(prospector=prospector)
        return render(request, 'indicacoes/indicacoes_lista.html', {'indicacoes': indicacoes})
    return redirect('')


def create_indicacao(request):
    indicacao = Indicacao.objects.create(nome="Minha Dieta2", usuario=request.user)

    form = IndicacaoForm(request.POST or None)
    form.usuario = request.user
    if form.is_valid():
        form.save()
        return redirect('list_indicacoes')
    return render(request, 'indicacoes/indicacao-form.html', {'form': form, 'indicacao': indicacao})


def update_indicacao(request, id):
    indicacao = Indicacao.objects.get(id=id)
    alimentos_indicacao = indicacao.alimentos.all()
    form = IndicacaoForm(request.POST or None, instance=indicacao)
    if form.is_valid():
        form.save()
        return redirect('list_indicacoes')
    return render(request, 'indicacoes/indicacao-form.html',
                  {'form': form, 'indicacao': indicacao, 'alimentos_indicacao': alimentos_indicacao})


def delete_indicacao(request, id):
    indicacao = Indicacao.objects.get(id=id)

    if request.method == "POST":
        print("delete indicacao post")
        indicacao.delete()
        return redirect('list_minhas_indicacoes')

    return render(request, 'indicacoes/confirm-indicacao-delete.html', {'indicacao': indicacao})


def add_alimento_indicacao(request, id_alimento, id_indicacao):
    indicacao = Indicacao.objects.get(id=id_indicacao)

    indicacao.save()

    indicacao_obj = serializers.serialize('json', [indicacao, ])

    return JsonResponse(indicacao_obj, safe=False)


def remove_alimento_indicacao(request, id_alimento, id_indicacao):
    indicacao = Indicacao.objects.get(id=id_indicacao)

    indicacao.save()

    indicacao_obj = serializers.serialize('json', [indicacao, ])

    return JsonResponse(indicacao_obj, safe=False)


@csrf_protect
def submit_indicacao(request):
    if request.POST:
        nome_indicado = request.POST.get('nome_indicado')
        telefone_indicado = request.POST.get('telefone_indicado')
        autorizado = request.POST.get('autorizado')
        if autorizado == 'on':
            autorizacao = True
        else:
            messages.error(request, "Não é possivel fazer uma solicitação sem a autorização do usuario")
            return redirect('/indicacoes/minhas_indicacoes/')

        prospector = Prospector.objects.get(usuario=request.user)

        indicacao = Indicacao.objects.create(nome_indicado=nome_indicado,
                                             prospector=prospector,
                                             telefone_indicado=telefone_indicado,
                                             autorizado=autorizacao)
        indicacao.save()

    return redirect('/indicacoes/minhas_indicacoes/')
