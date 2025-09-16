from django import forms
from .models import Viaje, Conductor, Empresa, Pasajero

class ViajeForm(forms.ModelForm):
    class Meta:
        model = Viaje
        fields = ['conductor', 'empresa', 'pasajeros', 'fecha', 'hora_salida_prog', 'hora_llegada_prog']
        widgets = {
            'pasajeros': forms.CheckboxSelectMultiple(),
            'fecha': forms.DateInput(attrs={'type': 'date'}),
            'hora_salida_prog': forms.TimeInput(attrs={'type': 'time'}),
            'hora_llegada_prog': forms.TimeInput(attrs={'type': 'time'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        hora_salida = cleaned_data.get('hora_salida_prog')
        hora_llegada = cleaned_data.get('hora_llegada_prog')
        if hora_salida and hora_llegada and hora_llegada <= hora_salida:
            raise forms.ValidationError("La hora de llegada debe ser posterior a la hora de salida.")
        return cleaned_data