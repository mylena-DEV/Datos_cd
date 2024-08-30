from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import DatosSerializer

class DatosViewSet (viewsets.ModelViewSet):
    queryset = Datos.objects.all()
    serializer_class = DatosSerializer
# Create your views here.
