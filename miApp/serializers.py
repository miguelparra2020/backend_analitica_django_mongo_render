from rest_framework import serializers
from .models import Usuarios

class UsuariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuarios
        fields = '__all__'  # Puedes especificar los campos que deseas incluir aquí
