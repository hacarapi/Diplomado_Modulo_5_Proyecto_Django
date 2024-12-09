from django.db import models
from django.core.exceptions import ValidationError
from datetime import datetime

# Validaciones personalizadas
def validar_placa(placa):
    if len(placa) < 6:
        raise ValidationError('La placa debe tener al menos 6 caracteres.')

class Vehiculo(models.Model):
    placa = models.CharField(max_length=10, unique=True, validators=[validar_placa])
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)

    def __str__(self):
        return self.placa

class Espacio(models.Model):
    numero = models.IntegerField(unique=True)
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return f'Espacio {self.numero}'

class Tarifa(models.Model):
    precio_hora = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f'${self.precio_hora}/hora'

class Registro(models.Model):
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE)
    espacio = models.ForeignKey(Espacio, on_delete=models.CASCADE)
    hora_entrada = models.DateTimeField(default=datetime.now)
    hora_salida = models.DateTimeField(null=True, blank=True)
    costo = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)

    def calcular_costo(self):
        if self.hora_salida:
            horas = (self.hora_salida - self.hora_entrada).seconds / 3600
            tarifa = Tarifa.objects.first()
            self.costo = round(horas * tarifa.precio_hora, 2)

    def save(self, *args, **kwargs):
        if self.hora_salida:
            self.calcular_costo()
        super().save(*args, **kwargs)
