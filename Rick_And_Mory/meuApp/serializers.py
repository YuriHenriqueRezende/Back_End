from rest_framework import serializers
from .models import *


class CharacteSerializer(serializers.ModelSerializer):
    class Meta:
        many = True
        model = Character
        fields = '__all__'


class Locationserializer(serializers.ModelSerializer):
    class Meta:
        many = True
        model = Location
        fields = '__all__'


class Episodeserializer(serializers.ModelSerializer):
    class Meta:
        many = True
        model = Episode
        fields = '__all__'
