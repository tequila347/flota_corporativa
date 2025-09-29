from django.urls import path
from . import views
app_name='f_c'

urlpatterns = [
    path('', views.index, name='index'),  # Ruta para la página principal
    path('registrar/', views.registrar_viaje, name='registrar_viaje'),
    path('login/', views.login_view, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.logout_view, name='logout'),
    # Agrega una URL para listar viajes si es necesario
    path('viajes/', views.lista_viajes, name='lista_viajes'),
] 