from .views  import *
from rest_framework.routers import DefaultRouter
from django.urls import path

router = DefaultRouter()
router.register(r'usuarios',UsuarioView)
router.register(r'fotos',fotoslivroView)
router.register(r'categoria',categoriasView)
router.register(r'livros',livroView)
router.register(r'emprestimos',emprestimoView)

urlpatterns = router.urls