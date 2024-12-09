from django.contrib import admin
from .models import Vehiculo, Espacio, Tarifa, Registro

admin.site.register(Vehiculo)
admin.site.register(Espacio)
admin.site.register(Tarifa)
admin.site.register(Registro)