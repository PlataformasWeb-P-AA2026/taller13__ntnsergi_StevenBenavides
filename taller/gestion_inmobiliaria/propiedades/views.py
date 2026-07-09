from django.shortcuts import render
from .models import Edificio, Departamento
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from .models import Edificio, Departamento
from .serializers import EdificioSerializer, DepartamentoSerializer

class EdificioViewSet(viewsets.ModelViewSet):
    queryset = Edificio.objects.all()
    serializer_class = EdificioSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]  # Bloquea el acceso si no hay Token

class DepartamentoViewSet(viewsets.ModelViewSet):
    queryset = Departamento.objects.all()
    serializer_class = DepartamentoSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

def index(request):
    return render(request, 'index.html')

def listar_edificios(request):
    edificios = Edificio.objects.all()
    return render(request, 'listar_edificios.html', {'edificios': edificios})

def listar_departamentos(request):
    departamentos = Departamento.objects.all()
    return render(request, 'listar_departamentos.html', {'departamentos': departamentos})