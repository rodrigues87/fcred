from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import logout as django_logout

from conta.models import Conta
from dados_bancarios.models import Dados_bancarios
from termos.models import Termos, Aceite
from usuarios.forms import UserForm
from usuarios.models import User, Prospector

# Create your views here.
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import get_user_model


def base(request):
    return render(request, 'base.html')


def login_user(request):
    return render(request, 'login/login.html')


@csrf_protect
def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User(email=username, password=password)
        result = user.logar(request)
        return result


@csrf_protect
def login_verificar(request):
    if request.POST:
        code = request.POST.get('code')
        conta = Conta.objects.get(usuario=request.user)
        conta.codigo_verificador_tentado = code
        resultado = conta.verificar_conta(request)
        return resultado

    return render(request, 'login/verificar_conta.html')


@csrf_protect
def submit_login_google(request):
    if request.POST and request.is_ajax():
        first_name = request.POST.get('first_name')
        imagem_url = request.POST.get('imagem_url')
        email = request.POST.get('email')

        password = User.objects.make_random_password()

        try:
            user = User.objects.get(email=email)
            user.set_password(password)
            user.save()
            user = authenticate(username=user.email, password=password)
            if user is not None:
                login(request, user)
                print("usuario logado...redirecionado para pagina inicial: " + password)

        except User.DoesNotExist:

            User.objects.create(first_name="first_name", imagem_url="imagem_url", email=email, password=password)
            user = authenticate(username=email, password=password)
            print("Usuario criado e esta autenticado")

    print("não entrou no post")
    return redirect('/')


def administrador(request):
    if request.user.is_authenticated:
        return render(request, 'index.html')
    else:
        return redirect('/pedidos/solicitar')


@login_required
def logout(request):
    if request.user.is_authenticated:
        django_logout(request)
        return redirect('/usuarios/login/')
    else:
        messages.error(request, "Usuário não está logado")
        return redirect('/usuarios/login/')


def list_usuarios(request):
    try:
        usuario = User.objects.get(usuario=request.user.id)
    except User.DoesNotExist:
        usuario = User.objects.create(nome="Minha Dieta", usuario=request.user)

    return render(request, 'usuarios_lista.html', {'usuario': usuario})


@csrf_protect
def register_prospector(request):
    global termo_vigente
    termos = Termos.objects.all()
    for termo in termos:
        termo_vigente = termo

    if request.POST:

        aceite = request.POST.get('aceite')

        if aceite == 'on':
            cpf = request.POST.get('cpf')
            celular = request.POST.get('celular')

            numero_banco = request.POST.get('numero_banco')
            nome_banco = request.POST.get('nome_banco')
            agencia = request.POST.get('agencia')
            conta = request.POST.get('conta')
            digito_conta = request.POST.get('digito_conta')

            aceite = Aceite(termo=termo_vigente, aceite=True)
            aceite.save()

            dados_bancarios = Dados_bancarios(numero_banco=numero_banco,
                                              nome_banco=nome_banco,
                                              agencia=agencia,
                                              conta=conta,
                                              digito_conta=digito_conta
                                              )
            dados_bancarios.save()

            prospector = Prospector(cpf=cpf, telefone_celular=celular, usuario=request.user,
                                    dados_bancarios=dados_bancarios,aceite=aceite)

            prospector.save()

            return redirect('/')
        else:
            messages.error(request, "É preciso aceitar os termos")
            return render(request, 'prospectores/register_prospector.html', {'termos': termos})

    return render(request, 'prospectores/register_prospector.html', {'termos': termos})


@csrf_protect
def create_usuario(request):
    if request.POST:
        # TODO preciso verificar aqui se o usuario já existe
        username = request.POST.get('username')
        password = request.POST.get('password')

        new_user = User(email=username)
        new_user.set_password(password)

        login_user = User(email=username, password=password)

        user = new_user.criar_usuario(request)
        if user is None:
            return render(request, 'login/register.html')
        conta = Conta(usuario=user)
        conta.criar_conta()

        messages.success(request, "Verifique a caixa de entrada do email")

        login_user.logar(request)
        return redirect('/usuarios/login/verificar')
    return render(request, 'login/register.html')


def update_usuario(request, id):
    usuario = User.objects.get(id=id)
    form = UserForm(request.POST or None, instance=usuario)
    if form.is_valid():
        form.save()
        return redirect('list_usuarios')
    return render(request, 'site/usuarios/usuario-form.html', {'form': form, 'usuario': usuario})


def delete_usuario(request, id):
    usuario = User.objects.get(id=id)

    if request.method == "POST":
        print("delete usuario post")
        usuario.delete()
        return redirect('list_usuarios')

    return render(request, 'site/usuarios/confirm-usuario-delete.html', {'usuario': usuario})
