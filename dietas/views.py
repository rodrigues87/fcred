from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect

from fcred.models import Alimento
from dietas.models import Dieta
from dietas.forms import DietaForm
from recomendado.models import Recomendado


def list_minhas_dietas(request):
    if request.user.is_authenticated:
        dietas = Dieta.objects.filter(usuario=request.user)
        return render(request, 'dietas/dietas_minha_lista.html', {'dietas': dietas})
    return redirect('/dietas/solicitar')


def list_dietas(request):
    if request.user.is_authenticated:
        dietas = Dieta.objects.all()
        return render(request, 'dietas/dietas_lista.html', {'dietas': dietas})
    return redirect('/dietas/solicitar')


def create_dieta(request):
    dieta = Dieta.objects.create(nome="Minha Dieta2", usuario=request.user)

    form = DietaForm(request.POST or None)
    form.usuario = request.user
    alimentos = Alimento.objects.all()
    if form.is_valid():
        form.save()
        return redirect('list_dietas')
    return render(request, 'dietas/dieta-form.html', {'form': form, 'dieta': dieta, 'alimentos': alimentos})


def update_dieta(request, id):
    alimentos = Alimento.objects.all()
    recomendacoes = Recomendado.objects.all()

    dieta = Dieta.objects.get(id=id)
    form = DietaForm(request.POST or None, instance=dieta)
    if form.is_valid():
        form.save()
        return redirect('list_dietas')
    return render(request, 'dietas/dieta-form.html', {'form': form, 'dieta': dieta, 'alimentos': alimentos,
                                                      'recomendacoes': recomendacoes})


def delete_dieta(request, id):
    dieta = Dieta.objects.get(id=id)

    if request.method == "POST":
        print("delete dieta post")
        dieta.delete()
        return redirect('list_minhas_dietas')

    return render(request, 'dietas/confirm-dieta-delete.html', {'dieta': dieta})


def add_alimento_dieta(request, id_alimento, id_dieta):
    print('entrou na funcao')

    alimento = Alimento.objects.get(id=id_alimento)
    dieta = Dieta.objects.get(id=id_dieta)

    dieta.alimentos.add(alimento)

    dieta.save()

    return HttpResponse("foi")


def remove_alimento_dieta(request, id_alimento, id_dieta):
    print('entrou na funcao')

    alimento = Alimento.objects.get(id=id_alimento)
    dieta = Dieta.objects.get(id=id_dieta)

    dieta.alimentos.remove(alimento)

    dieta.save()

    return HttpResponse("foi")

@csrf_protect
def submit_dieta(request):
    if request.POST:
        nome = request.POST.get('nomeDieta')
        observacao = request.POST.get('observacao')
        user = request.user

        dieta = Dieta.objects.create(nome=nome,observacao=observacao,usuario=user)

    return redirect('/dietas/update/'+str(dieta.id))
