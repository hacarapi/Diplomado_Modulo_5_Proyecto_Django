from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Vehiculo, Espacio, Tarifa, Registro
from .serializers import VehiculoSerializer, EspacioSerializer, TarifaSerializer, RegistroSerializer

class VehiculoViewSet(ModelViewSet):
    queryset = Vehiculo.objects.all()
    serializer_class = VehiculoSerializer

class EspacioViewSet(ModelViewSet):
    queryset = Espacio.objects.all()
    serializer_class = EspacioSerializer

class TarifaViewSet(ModelViewSet):
    queryset = Tarifa.objects.all()
    serializer_class = TarifaSerializer

class RegistroViewSet(ModelViewSet):
    queryset = Registro.objects.all()
    serializer_class = RegistroSerializer

@api_view(['GET'])
def verificar_espacio_disponible(request):
    disponible = Espacio.objects.filter(disponible=True).exists()
    return Response({'espacio_disponible': disponible})
