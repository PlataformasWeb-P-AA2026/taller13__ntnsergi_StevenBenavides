from django.shortcuts import render
from .models import Edificio, Departamento

def listar_edificios(request):
    edificios = Edificio.objects.all()
    return render(request, 'tabla_edificios.html', {'edificios': edificios})

def listar_departamentos(request):
    departamentos = Departamento.objects.all()
    return render(request, 'tabla_departamentos.html', {'departamentos': departamentos})