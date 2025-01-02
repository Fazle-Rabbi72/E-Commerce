from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DepartmentViewSet, CategoryViewSet, ColorViewSet, ProductViewSet, ProductImageViewSet

router = DefaultRouter()
router.register('departments', DepartmentViewSet)
router.register('categories', CategoryViewSet)
router.register('colors', ColorViewSet)
router.register('products', ProductViewSet)
router.register('product-images', ProductImageViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
