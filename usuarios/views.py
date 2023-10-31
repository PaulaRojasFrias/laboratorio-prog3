from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse


# Create your views here.


def index_admin(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("usuarios:login_view"))
    return render(request, 'usuarios/home.html')


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return HttpResponseRedirect(reverse("usuarios:index_admin"))
        else:
            return render(request, "usuarios/login.html", {"msj": "Usuario o contraseña incorrecta"})

    return render(request, 'usuarios/login.html')


def logout_view(request):
    logout(request)
    return render(request, "usuarios/login.html", {
        "msj": "Usuario Deslogueado"})
