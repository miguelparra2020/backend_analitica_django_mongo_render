

# Create your views here.
from rest_framework import generics
from .models import Usuarios
from .serializers import UsuariosSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

from . import requests_functions  # Importa las funciones de requests

class UsuariosListCreate(generics.ListCreateAPIView):
    queryset = Usuarios.objects.all()
    serializer_class = UsuariosSerializer


@api_view(['POST'])
def insertar_usuario(request):
    if request.method == 'POST':
        data = request.data  # Obtiene los datos del cuerpo de la solicitud POST
        resultado_insertar = requests_functions.insertar_usuario(data)
        return Response(resultado_insertar)

@api_view(['GET'])
def obtener_usuarios(request):
    resultado_obtener = requests_functions.obtener_usuarios()
    return Response(resultado_obtener)

@api_view(['POST'])
def delete_usuarios(request):
    if request.method == 'POST':
        data = request.data  # Obtiene los datos del cuerpo de la solicitud POST
        resultado_delete = requests_functions.delete_usuarios()
        return Response(resultado_delete)

