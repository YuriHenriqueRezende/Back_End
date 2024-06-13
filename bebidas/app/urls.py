from .views import *
from rest_framework.routers import DefaultRouter
from django.urls import path

router = DefaultRouter()
router.register(r'categoria-produtos',CategoriaProdutosView)
router.register(r'produtos',ProdutosView)
router.register(r'vendas',VendasView)
router.register(r'vendas-produtos',VendasProdutosView)
router.register(r'usuarios',UsuarioCustomizadoView)

urlpatterns = router.urls



