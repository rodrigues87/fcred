from allauth.socialaccount.models import SocialAccount
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from recomendado.models import Recomendado
from recomendado.forms import RecomendadoForm
from dietas.models import Dieta


def index(request):
    return render(request, 'index.html')


@login_required(login_url='/usuarios/login/')
def list_recomendado(request):
    recomendado = Recomendado.objects.all()
    return render(request, 'recomendado/recomendados_lista.html', {'recomendado': recomendado})


def create_alimento(request):
    form = RecomendadoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('list_recomendado')
    return render(request, 'dietas/dieta-form.html', {'form': form})


def update_alimento(request, id):
    recomendado = Recomendado.objects.get(id=id)
    form = RecomendadoForm(request.POST or None, instance=recomendado)
    if form.is_valid():
        form.save()
        return redirect('list_recomendado')
    return render(request, 'recomendado/recomendado-form.html', {'form': form, 'recomendado': recomendado})


def delete_alimento(request, id):
    recomendado = Recomendado.objects.get(id=id)

    if request.method == "POST":
        print("delete recomendado post")
        recomendado.delete()
        return redirect('list_recomendado')

    return render(request, 'recomendado/confirm-recomendado-delete.html', {'recomendado': recomendado})



