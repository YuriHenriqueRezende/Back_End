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
    
    def post(self,request):
        usuarioJson = request.data
        usuarioSerializerd = usuarioSerializer(data=usuarioJson)
        usuarioSerializerd.is_valid(raise_exception=True)
        usuarioSerializerd.save()
        return Response(status=201, data=usuarioSerializerd.data)

    def put(self, request, usuarioId = ''):
        usuarioFound = None

        try:
            usuarioFound = usuario.objects.get(id=usuarioId)
        except usuario.DoesNotExist:
            return Response(status=404,data='Usuario not Found!')

        usuarioJson = request.data
        usuarioSerializerd = usuarioSerializer(usuarioFound,data=usuarioJson)
        usuarioSerializerd.is_valid(raise_exception=True)
        usuarioSerializerd.save()
        return Response(status=200,data=usuarioSerializerd.data)
    
    def delete(self,request, usuarioId = ''):
        usuarioFound = None
        try:
            usuarioFound = usuario.objects.get(id=usuarioId)
        except usuario.DoesNotExist:
            return Response(status=404,data='Usuario Not Found!')
        usuarioFound.delete()
        return Response(status=200,data='Usuario successfully deleted!')
    



class registroPIView(APIView):
    def get(self, request, registroId = ''):
        if registroId == '':
            registroId = ''
            if 'nome_da_maquina' in request.GET and 'status' in request.GET:
                registroFound = registro.objects.filter(nome_da_maquina__gt=request.GET['nome_da_maquina']).filter(status__contains=request.GET['status'])
            elif 'nome_da_maquina' in request.GET:
                registroFound = registro.objects.filter(nome_da_maquina__gt=request.GET['nome_da_maquina'])
            elif 'status' in request.GET:
                registroFound = registro.objects.filter(status__contains=request.GET['status'])
            else:
                registroFound = registro.objects.all()
            registroSerializerd = registroSerializer(registroFound, many=True)
            return Response(registroSerializerd.data)
        else:
            try:
                registroFound = registro.objects.get(id=registroId)
                registroSerialized = registroSerializer(registroFound, many=False)
                return Response(registroSerialized.data)
            except:
                return Response(status=404, data='Usuario Not Found!')

    def post(self,request):
        registroJson = request.data
        registroSerializerd = registroSerializer(data=registroJson)
        registroSerializerd.is_valid(raise_exception=True)
        registroSerializerd.save()
        return Response(status=201, data=registroSerializerd.data)

    def put(self, request, registroId = ''):
        registroFound = None

        try:
            registroFound = registro.objects.get(id=registroId)
        except registro.DoesNotExist:
            return Response(status=404,data='Usuario not Found!')

        registroJson = request.data
        registroSerializerd = registroSerializer(registroFound,data=registroJson)
        registroSerializerd.is_valid(raise_exception=True)
        registroSerializerd.save()
        return Response(status=200,data=registroSerializerd.data)

    def delete(self,request, registroId = ''):
        registroFound = None
        try:
            registroFound = registro.objects.get(id=registroId)
        except registro.DoesNotExist:
            return Response(status=404,data='Usuario Not Found!')
        registroFound.delete()
        return Response(status=200,data='Usuario successfully deleted!')
