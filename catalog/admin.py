  # catalog/admin.py
from django.contrib import admin
from .models import Category
from .models import Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Админка для модели Category"""
    list_display = ("id", "name",)  # Выводим id и name в списке
    list_filter = ("name",)  # Фильтрация по имени (не обязательно)
    search_fields = ("name", "description",)  # Поиск по имени и описанию


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Админка для модели Product"""
    list_display = ("id", "name", "price", "category",)  # Выводим id, name, price, category в списке
    list_filter = ("category",)  # Фильтрация продуктов по категории
    search_fields = ("name", "description",)  # Поиск по name и description
