from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import DatosSerializer, CiudadSerializer


class DatosViewSet (viewsets.ModelViewSet):
    queryset = Datos.objects.all()
    serializer_class = DatosSerializer
class CiudadViewSet (viewsets.ModelViewSet):
    queryset = Ciudad.objects.all()
    serializer_class = CiudadSerializer
# Create your views here.
