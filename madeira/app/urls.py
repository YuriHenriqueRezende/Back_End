from .views  import *
from rest_framework.routers import DefaultRouter
from django.urls import path

router = DefaultRouter()
router.register(r'usuarios',UsuarioView)
router.register(r'pecas',pecasView)
router.register(r'produto',produtoView)
router.register(r'carrinho',carrinhoView)
router.register(r'pagamento',pagamentoView)
router.register(r'pedidos',pedidosView)
router.register(r'imagem',imagemView)

urlpatterns = router.urls