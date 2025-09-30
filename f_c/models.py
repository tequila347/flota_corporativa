from django.db import models
from datetime import datetime 
from django.contrib.auth.models import User

class Empresa(models.Model):
    """Se crea la clase Empresa para almacenar datos basicos de la misma """
    id=models.BigAutoField(auto_created=True, primary_key=True,serialize=False, verbose_name='ID')
    n_empresa=models.CharField(max_length=200, verbose_name='Empresa')
    rut=models.IntegerField(verbose_name='RUT', unique=True)
    direccion=models.CharField(max_length=200, verbose_name='DIRECCION')
    c_electronico=models.EmailField(verbose_name='e-mail',unique=True)
    class Meta:
        verbose_name='Empresa'
        verbose_name_plural='Empresas'


    def __str__(self):
        """Devuelve una representacion del modelo en cadena"""
        return f'Empresa: {self.n_empresa} Id: {self.id}'

class Pasajero(models.Model):
    """Se crea la clase Pasajero para almacenar datos basico del mismo"""
    id=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    n_pasajero=models.CharField(max_length=200, verbose_name='Nombre')
    a_pasajero=models.CharField(max_length=200, verbose_name='Apellido')
    empresa=models.ForeignKey(Empresa, on_delete=models.CASCADE)
    telefono=models.CharField(max_length=15)
    class Meta:
        verbose_name='Pasajero'
        verbose_name_plural='Pasajeros'

    def __str__(self):
        """Devuelve una representacion del modelo en cadena"""
        return f'Nombre: {self.n_pasajero} Apellido: {self.a_pasajero} Empresa: {self.empresa} iD: {self.id}'

class Conductor(models.Model):
    """Se crea la clase Conductor para almacenar datos basicos del mismmo"""
    id=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    n_conductor=models.CharField(max_length=200, verbose_name='Nombre')
    a_conductor=models.CharField(max_length=200, verbose_name='Apellido')
    telefono=models.CharField(max_length=12, verbose_name='Telefono')
    class Meta:
        verbose_name='Conductor'
        verbose_name_plural='Conducotres'


    def __str__(self):
        """Devuelve una representacion del modelo en cadena"""   
        return f'Nombre: {self.n_conductor},Apellido: {self.a_conductor}'

class Viaje(models.Model):
    """Clase Viaje: Almacena informacion de cada traslado"""
    id= models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    conductor=models.ForeignKey(Conductor, on_delete=models.CASCADE, verbose_name='Conductor')
    empresa=models.ForeignKey(Empresa, on_delete=models.CASCADE, verbose_name='Empresa')
    pasajeros=models.ManyToManyField(Pasajero,related_name='viajes',verbose_name='pasajeros')
    fecha=models.DateField(verbose_name='Fecha de Viaje')
    hora_salida_prog=models.TimeField(verbose_name='Hora de salida programada')
    hora_salida_real=models.TimeField(verbose_name='hora de salida real',null=True, blank=True)
    hora_llegada_prog=models.TimeField(verbose_name='Hora de llegada programada')
    hora_llegada_real=models.TimeField(verbose_name='Hora de llegada real',null=True, blank=True)
    class Meta:
        verbose_name='Viaje'
        verbose_name_plural='Viajes'


    def __str__(self):
        """Devuelve una representacion del modelo en cadena"""
        return f'Viaje {self.id} - Conductor: {self.conductor.n_conductor} {self.conductor} - Fecha: {self.fecha}'
    
    def puntualidad_salida(self):
        """Devuelve diferencia en minutos entre hora programada y real de la salida"""
        if self.hora_llegada_real:
            delta=(datetime.combine(self.fecha, self.hora_llegada_real) - 
                   datetime.combine(self.fecha, self.hora_llegada_prog))
            return delta.total_seconds() / 60
        return None
    
class PerfilUsuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    domicilio = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"Perfil de {self.user.username}"

 
    
