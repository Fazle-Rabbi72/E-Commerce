from django.contrib import admin
from .models import Department, Category, Color, Product, ProductImage

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'department']
    list_filter = ['department']
    search_fields = ['name']

@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'hex_code']
    search_fields = ['name', 'hex_code']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'name', 'price', 'quantity', 'off_percentage', 
        'discounted_price', 'category', 'brand', 'ratings', 
        'created_at', 'updated_at'
    ]
    list_filter = ['category', 'brand', 'ratings']
    search_fields = ['name', 'brand']
    filter_horizontal = ['colors', 'additional_images']

@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'product', 'image']
