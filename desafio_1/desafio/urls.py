from django.urls import path
from .views import *

urlpatterns = [
    path("usuarios/", usuarioAPIView.as_view(), name='usuarios'),
    path("usuarios/<int:usuarioId>", usuarioAPIView.as_view(),name='usuariosParametro'),
    path("registro/", registroPIView.as_view(), name='registro'),
    path("registro/<int:registroId>", registroPIView.as_view(),name='registroParametro'),
]