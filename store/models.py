from django.db import models

# Категория для обычных товаров
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Обычные товары (раздел "Тауарлар")
class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='products/', blank=True, null=True)

    def __str__(self):
        return self.name

# 🔥 Скидочные товары (отображаются на главной странице)
class DiscountProduct(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    old_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='discounts/', blank=True, null=True)

    def __str__(self):
        return f"{self.name} (Жеңілдік)"
