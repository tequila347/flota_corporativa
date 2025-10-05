from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import PerfilUsuario, Viaje


def index(request):
    return render(request, 'viajes/index.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f"Bienvenido, {username}!")
            return redirect('f_c:dashboard')
        else:
            messages.error(request, "Usuario o contraseña incorrectos.")
            return render(request, 'viajes/login.html')
    return render(request, 'viajes/login.html')

def dashboard(request):
    if not request.user.is_authenticated:
        return redirect('f_c:login')
    return render(request, 'viajes/dashboard.html', {'user': request.user})

def logout_view(request):
    logout(request)
    messages.success(request, "Has cerrado sesión correctamente.")
    return redirect('f_c:index')

def registro_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        domicilio = request.POST.get('domicilio')

        if password1 != password2:
            messages.error(request, "Las contraseñas no coinciden.")
            return render(request, 'viajes/registro.html')

        if User.objects.filter(username=username).exists():
            messages.error(request, "El nombre de usuario ya está en uso.")
            return render(request, 'viajes/registro.html')

        if User.objects.filter(email=email).exists():
            messages.error(request, "El correo electrónico ya está registrado.")
            return render(request, 'viajes/registro.html')

        # Crear el usuario
        user = User.objects.create_user(username=username, email=email, password=password1)
        # Crear el perfil con el domicilio
        PerfilUsuario.objects.create(user=user, domicilio=domicilio)
        # Iniciar sesión automáticamente
        login(request, user)
        messages.success(request, f"Registro exitoso, {username}!")
        return redirect('f_c:dashboard')

    return render(request, 'viajes/registro.html')

def lista_viajes(request):
    viajes = Viaje.objects.all()
    return render(request, 'viajes/lista_viajes.html', {'viajes': viajes})

def registrar_viaje(request):
    if request.method == 'POST':
        form = Viaje(request.POST)
        if form.is_valid():
            form.save()
            return redirect('f_c:lista_viajes')  # Usa el namespace f_c
    else:
        form = Viaje()
    return render(request, 'viajes/registrar_viaje.html', {'form': form})

def viajes_view(request):
    if not request.user.is_authenticated:
        return redirect('f_c:login')
    if request.method == 'POST':
        form = Viaje(request.POST)
        if form.is_valid():
            viaje = form.save(commit=False)
            viaje.user = request.user  # Asociar el viaje al usuario autenticado
            viaje.save()
            messages.success(request, "Viaje registrado correctamente.")
            return redirect('f_c:dashboard')
        else:
            messages.error(request, "Por favor, corrige los errores en el formulario.")
    else:
        form = Viaje()
    return render(request, 'viajes/registrar_viaje.html', {'form': form})