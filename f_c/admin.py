from django.contrib import admin
from .models import Empresa, Pasajero, Conductor, Viaje

@admin.register(Empresa)
class EmpresaAdmin(admin.ModelAdmin):
    list_display = ('n_empresa', 'rut', 'direccion', 'c_electronico')

@admin.register(Pasajero)
class PasajeroAdmin(admin.ModelAdmin):
    list_display = ('n_pasajero', 'a_pasajero', 'empresa', 'telefono')

@admin.register(Conductor)
class ConductorAdmin(admin.ModelAdmin):
    list_display = ('n_conductor', 'a_conductor', 'telefono')

@admin.register(Viaje)
class ViajeAdmin(admin.ModelAdmin):
    list_display = ('id', 'conductor', 'empresa', 'fecha', 'hora_salida_prog', 'hora_llegada_prog')
    filter_horizontal = ('pasajeros',)
    list_filter = ('fecha', 'conductor', 'empresa')
    search_fields = ('conductor__n_conductor', 'empresa__n_empresa')