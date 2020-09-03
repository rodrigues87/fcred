from allauth.socialaccount.models import SocialAccount
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from core.models import Alimento
from core.forms import AlimentoForm
from dietas.models import Dieta


def index(request):
    return render(request, 'index.html')


@login_required(login_url='/usuarios/login/')
def list_alimentos(request):
    alimentos = Alimento.objects.all()
    return render(request, 'alimentos/alimentos_lista.html', {'alimentos': alimentos})


def create_alimento(request):
    form = AlimentoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('list_alimentos')
    return render(request, 'dietas/dieta-form.html', {'form': form})


def update_alimento(request, id):
    alimento = Alimento.objects.get(id=id)
    form = AlimentoForm(request.POST or None, instance=alimento)
    if form.is_valid():
        form.save()
        return redirect('list_alimentos')
    return render(request, 'alimentos/alimento-form.html', {'form': form, 'alimento': alimento})


def delete_alimento(request, id):
    alimento = Alimento.objects.get(id=id)

    if request.method == "POST":
        print("delete alimento post")
        alimento.delete()
        return redirect('list_alimentos')

    return render(request, 'alimentos/confirm-alimento-delete.html', {'alimento': alimento})



