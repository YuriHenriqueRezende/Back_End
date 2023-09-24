from django.shortcuts import render
from .serializers import *
from rest_framework.views import APIView # Manual #
from rest_framework.viewsets import ModelViewSet # Automatico #
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated

class usuarioAPIView(APIView):
    def get(self, request, usuarioId = ''):
        if usuarioId == '':
            usuarioFould = ''
            if 'nome' in request.GET and 'CPF' in request.GET:
                usuarioFould = usuario.objects.filter(nome__gt=request.GET['nome']).filter(CPF__contains=request.GET['CPF'])
            elif 'nome' in request.GET:
                usuarioFould = usuario.objects.filter(nome__gt=request.GET['nome'])
            elif 'CPF' in request.GET:
                usuarioFould = usuario.objects.filter(CPF__contains=request.GET['CPF'])
            else:
                usuarioFould = usuario.objects.all()
            usuarioSerializerd = usuarioSerializer(usuarioFould, many=True)
            return Response(usuarioSerializerd.data)
        else:
            try:
                usuarioFould = usuario.objects.get(id=usuarioId)
                usuarioSerializerd = usuarioSerializer(usuarioFould, many=False)
                return Response(usuarioSerializerd.data)
            except:
                return Response(status=404, data='Usuario Not Found!')


class registroPIView(APIView):
    def get(self, request, registroId = ''):
        if registroId == '':
            registroFound = registro.objects.all()
            registroSerialized = registroSerializer(registroFound, many=True)
            return Response(registroSerialized.data)
        else:
            try:
                registroFound = registro.objects.get(id=registroId)
                registroSerialized = registroSerializer(registroFound, many=False)
                return Response(registroSerialized.data)
            except:
                return Response(status=404, data='Usuario Not Found!')
