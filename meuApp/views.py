from django.shortcuts import render

# Create your views here.from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response

class CharacterAPIView(APIView):
    def get(self, request, CharacterId = ''):
        #se o get não tiver o filtro de id:
        if CharacterId == '':   
            characterFound = ''
            if 'name' in request.GET:
                namefilter = request.GET['name']
                characterFound = Character.objects.filter(name__contains=namefilter)
            elif 'location' in request.GET:
                namefilter = request.GET['location']
                characterFound = Character.objects.filter(name__contains=namefilter)
            else:
                characterFound = Character.objects.all() 
            serializer = CharacteSerializers(characterFound, many=True) 
            return Response(status=200, data=serializer.data)
        try:
            characterFound = Character.objects.get(id=CharacterId) 
            serializer = CharacteSerializers(characterFound, many=False) 
            return Response(status=200,data=serializer.data)
        except Character.DoesNotExist:
            return Response(status=404, data="oi")
    
    def post(self, request):
        characterJson = request.data
        CharacterSerialized = CharacteSerializers(data=characterJson,many=False)
        if CharacterSerialized.is_valid():
            CharacterSerialized.save()
            return Response(status=203, data=CharacterSerialized.data)
        return Response(status=400, data='burro')

    def delete(self,request, CharacterId=''):
        if (CharacterId != ''):
            characterFound = Character.objects.get(id=CharacterId)
            characterFound.delete()
            return Response(status=200, data='deu certo')
        return Response(status=400,data='faz direito animal')
    
    def put(self, request, CharacterId=''):
        if (CharacterId != ''):
            CharacterFoud = Character.objects.get(id=CharacterId)
            CharacterUpdateJSON = request.data
            SerializersCharacte = CharacteSerializers(CharacterFoud,data=CharacterUpdateJSON)

            if(SerializersCharacte.is_valid()):
                SerializersCharacte.save()
                return Response(status=200,data=SerializersCharacte.data)
            return Response(status=400,data='burro')
        return Response(status=400,data='faz direito animal')
        
class LocationAPIView(APIView):
    def get(self, request):
        LocationFound = Location.objects.all() 
        serializer = Locationserializer(LocationFound, many=True) 
        return Response(serializer.data) 


class EpisodeAPIView(APIView):
    def get(self, request):
        EpisodeFound = Episode.objects.all() 
        serializer = Episodeserializer(EpisodeFound, many=True) 
        return Response(serializer.data) 
