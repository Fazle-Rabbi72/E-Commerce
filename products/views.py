from rest_framework.viewsets import ModelViewSet
from .models import Department, Category, Color, Product, ProductImage
from .serializers import (
    DepartmentSerializer,
    CategorySerializer,
    ColorSerializer,
    ProductSerializer,
    ProductImageSerializer,
)

class DepartmentViewSet(ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ColorViewSet(ModelViewSet):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all().select_related('category').prefetch_related('colors', 'additional_images')
    serializer_class = ProductSerializer

class ProductImageViewSet(ModelViewSet):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer
