from django.shortcuts import render, redirect
from .models import Viaje
from .forms import ViajeForm

def index(request):
    return render(request, 'viajes/index.html')

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
