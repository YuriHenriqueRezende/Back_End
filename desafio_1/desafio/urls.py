from django.urls import path

from .views import *

urlpatterns = [
    path("usuarios/", usuarioAPIView.as_view(), name='usuarios'),
    path("usario/<int:usuarioId>", usuarioAPIView.as_view(),name='usuarioParametro')
#    path("registro/", registroPIView.as_view(), name='registro'),
]