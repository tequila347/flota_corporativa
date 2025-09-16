from django.urls import path
from . import views
app_name='f_c'

urlpatterns = [
    path('registrar/', views.registrar_viaje, name='registrar_viaje'),
    # Agrega una URL para listar viajes si es necesario
    path('viajes/', views.lista_viajes, name='lista_viajes'),
]