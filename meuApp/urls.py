# biblioteca p/ trabalhar com as rotas/endpoints
from django.urls import path

# importando tudo o que tem nas nossas views
from .views import *

urlpatterns = [
    path('Character/', CharacterAPIView.as_view(), name="Character"),
    path('Character/<int:CharacterId>',
         CharacterAPIView.as_view(), name="CharacterById"),
    path('Location/', LocationAPIView.as_view(), name="Location"),
    path('Episode/', EpisodeAPIView.as_view(), name="Episode"),
]
