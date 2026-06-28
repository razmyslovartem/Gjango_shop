# catalog/models.py
from django.db import models


class Category(models.Model):
    """Модель категории товаров."""

    name = models.CharField(max_length=100, verbose_name="Наименование")
    description = models.TextField(default="Описание отсутствует", verbose_name="Описание категории")

    def __str__(self):
        """Строковое представление объекта (для админки, shell)."""
        return self.name

    class Meta:
        """Метаданные модели (настройки таблицы БД)."""

        verbose_name = "категория"  # Имя в единственном числе.
        verbose_name_plural = "категории"  # Имя во множественном числе.
        ordering = ["name"]  # Сортировка по алфавиту.


class Product(models.Model):
    """Модель товаров."""

    name = models.CharField(max_length=200, verbose_name="Наименование")
    description = models.TextField(default="Описание отсутствует", verbose_name="Описание товара")
    image = models.ImageField(
        upload_to="products/",  # папка загрузки в MEDIA_ROOT
        blank=True,  # Необязательное в формах Django
        null=True,  # Может быть NULL в БД PostgreSQL
        verbose_name="Изображение",
    )
    category = models.ForeignKey(
        Category,  # Связь с моделью Category.
        on_delete=models.CASCADE,  # При удалении категории -> удалить товары.
        related_name="products",  # Обратная связь: category.products.all().
        verbose_name="Категория",
    )
    price = models.DecimalField(  # FloatField - ошибки округления -> DecimalField.
        max_digits=10,  # Всего цифр (включая дробную часть).
        decimal_places=2,  # Цифр после запятой (копейки).
        verbose_name="Цена за покупку",
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")  # Автоматически при создании.
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name="Дата последнего изменения"  # Автоматически при каждом сохранении.
    )

    def __str__(self):
        """Строковое представление объекта (для админки, shell)."""
        return self.name

    class Meta:
        """Метаданные модели (настройки таблицы БД)."""

        verbose_name = "продукт"  # Имя в единственном числе.
        verbose_name_plural = "продукты"  # Имя во множественном числе.
        ordering = ["-created_at"]  # Сортировка от новых к старым.
