from django.shortcuts import render, redirect
from .models import Viaje
from .forms import ViajeForm

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

def lista_viajes(request):
    viajes = Viaje.objects.all()
    return render(request, 'viajes/lista_viajes.html', {'viajes': viajes})

def registrar_viaje(request):
    if request.method == 'POST':
        form = ViajeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('f_c:lista_viajes')  # Usa el namespace f_c
    else:
        form = ViajeForm()
    return render(request, 'viajes/registrar_viaje.html', {'form': form})
