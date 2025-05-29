from django.contrib import admin
from .models import Product, Category, DiscountProduct

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category')
    list_filter = ('category',)
    search_fields = ('name',)

admin.site.register(Category)

@admin.register(DiscountProduct)
class DiscountProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'old_price', 'price')
    search_fields = ('name',)
