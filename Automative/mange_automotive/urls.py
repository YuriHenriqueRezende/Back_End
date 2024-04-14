from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'usuario',usuarioAPIView)
router.register(r'funcionario',funcionarioAPIView)
router.register(r'categoria_servico',categoria_servicoAPIView)
router.register(r'logistica_loja',logistica_lojaAPIView)
router.register(r'categoria_automovel',categoria_automovelAPIView)
router.register(r'manuntencao',manuntencaoAPIView)
router.register(r'posto_trabalho',posto_trabalhoAPIView)
router.register(r'pagamento',pagamentoAPIView)
router.register(r'reserva',reservaAPIView)



urlpatterns = router.urls
