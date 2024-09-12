from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse


# Create your views here.
def registrar_usuario(request, template_name='user/registrar.html'):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        tipo = request.POST['tipo_usuario']
        if tipo == 'administrador':
            user = User.objects.create_user(username, email, password)
            user.is_staff=True
            user.save()
        else:
            user = User.objects.create_user(username, email, password)
        return redirect('listar_usuario')

    return render(request, template_name, {})

def listar_usuario(request, template_name='user/listar.html'):
    usuarios = User.objects.all()
    usuario = {'lista':usuarios}
    return render(request, template_name, usuario)

def logar(request, template_name='user/login.html'):
    next = request.GET.get('next', '/listar_usuario/')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(next)
        else:
            return HttpResponseRedirect(settings.LOGIN_URL)
        
    return render(request, template_name, {'redirect_to':next})

def remover_usuario(request, pk, template_name='user/delete.html'):
    user = request.user
    if user.has_perm('user_delete_user'):
        try:
            usuario = User.objects.get(pk=pk)
            if request.method == 'POST':
                usuario.delete()
                return redirect('listar_usuario')
        except:
            return HttpResponse('Usuário não encontrado')
    else:
        return HttpResponse('Permissão negada')
    
    return render(request, template_name, {'usuario':usuario})


def deslogar(request):
    logout(request)
    return HttpResponseRedirect(settings.LOGIN_URL)