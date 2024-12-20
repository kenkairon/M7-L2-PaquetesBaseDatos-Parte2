from django.shortcuts import render
from .models import Cliente, Reserva
# Create your views here.

def listar_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'lista_clientes.html', {'clientes': clientes})

def listar_reservas(request):
    reservas = Reserva.objects.all()
    return render(request, 'lista_reservas.html', {'reservas': reservas})