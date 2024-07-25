from rest_framework import serializers
from .models import *

class usuarioSerializer(serializers.ModelSerializer):
    class Meta:
        many = True
        model = usuario
        fields = '__all__'

class registroSerializer(serializers.ModelSerializer):
    class Meta:
        many = True
        model = registro
        fields = '__all__'