from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100)
    department = models.OneToOneField(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Color(models.Model):
    name = models.CharField(max_length=50) 
    hex_code = models.CharField(max_length=7, blank=True, null=True)  

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)  
    description = models.TextField() 
    colors = models.ManyToManyField(Color, blank=True, related_name="products")  
    brand = models.CharField(max_length=100, blank=True, null=True) 
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products") 
    price = models.DecimalField(max_digits=10, decimal_places=2) 
    quantity = models.PositiveIntegerField(default=0) 
    off_percentage = models.DecimalField(
        max_digits=5, decimal_places=2, default=0.00
    ) 
    images = models.ImageField(upload_to="products/", blank=True, null=True)  
    additional_images = models.ManyToManyField(
        "ProductImage", blank=True, related_name="product_images"
    )  
    ratings = models.IntegerField(
        choices=[(i, f"{i} Star") for i in range(1, 6)], blank=True, null=True
    ) 
    created_at = models.DateTimeField(auto_now_add=True)  
    updated_at = models.DateTimeField(auto_now=True)  

    def __str__(self):
        return self.name

    def discounted_price(self):
        discount = (self.price * self.off_percentage) / 100
        return self.price - discount


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="product_images/")

    def __str__(self):
        return f"Image for {self.product.name}"
