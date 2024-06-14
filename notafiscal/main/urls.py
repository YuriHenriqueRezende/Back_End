from .views import *
from rest_framework.routers import DefaultRouter
from django.urls import path

router = DefaultRouter()
router.register(r'custom-users',CustomUserView)
router.register(r'product-category',ProductCategoryView)
router.register(r'product',ProductView)
router.register(r'invoice',InvoiceView)
router.register(r'invoice-item',InvoiceItemView)
router.register(r'warranty',WarrantyView)

urlpatterns = router.urls