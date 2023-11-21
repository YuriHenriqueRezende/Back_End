from rest_framework import serializers
from .models import *

class AssinaturaSerializer(serializers.ModelSerializer):
    class Meta:
        many = True
        model = Assinatura
        fields = '__all__'


class UsuariosGETSerializer(serializers.ModelSerializer):
    idAssinaturaFK = AssinaturaSerializer(read_only=True)
    class Meta:
        many = True
        model = Usuarios
        fields = '__all__'

class UsuariosSerializer(serializers.ModelSerializer):
    class Meta:
        many = True
        model = Usuarios
        fields = '__all__'
    


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        many = True
        model = Categoria
        fields = '__all__'


class FilmesGETSerializer(serializers.ModelSerializer):
    idCategoriaFK = CategoriaSerializer(read_only=True)
    
    class Meta:
        many = True
        model = Filmes
        fields = '__all__'

class FilmesSerializer(serializers.ModelSerializer):
    class Meta:
        many = True
        model = Filmes
        fields = '__all__'

class FavoritosGETSerializer(serializers.ModelSerializer):
    idFilmeFK = FilmesSerializer(read_only=True)
    idUsuarioFK = UsuariosSerializer(read_only=True)
    class Meta:
        many = True
        model = Favoritos
        fields = '__all__'

class FavoritosSerializer(serializers.ModelSerializer):
   
    class Meta:
        many = True
        model = Favoritos
        fields = '__all__'

