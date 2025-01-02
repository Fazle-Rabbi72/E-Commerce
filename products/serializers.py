from rest_framework import serializers
from .models import Department, Category, Color, Product, ProductImage

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    department_name = serializers.SerializerMethodField()
    class Meta:
        model = Category
        fields = ['id', 'name', 'department', 'department_name']

    def get_department_name(self, obj):
        return obj.department.name

        
class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = '__all__'

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    discounted_price = serializers.SerializerMethodField() 

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'colors', 'brand', 'category', 'price', 'quantity', 
                  'off_percentage', 'images', 'additional_images', 'ratings', 'created_at', 'updated_at', 
                  'discounted_price'] 

    def get_discounted_price(self, obj):
        return obj.discounted_price()