# catalog/models.py
from django.conf import settings
from django.db import models


class Category(models.Model):
    """Класс модели категории товаров."""

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
    """Класс модели товаров."""

    name = models.CharField(max_length=200, verbose_name="Наименование")
    description = models.TextField(default="Описание отсутствует", verbose_name="Описание товара")
    image = models.ImageField(
        upload_to="products/",  # папка загрузки в MEDIA_ROOT
        blank=True,  # Необязательное в формах Django
        null=True,  # Может быть NULL в БД PostgreSQL
        verbose_name="Изображение",
        help_text="Загрузи фото товара",
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

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,  # Ссылка на кастомного пользователя без жёткой привязки к классу.
        on_delete=models.CASCADE,
        verbose_name="Владелец",
        help_text="Кто создал эту карточку товара",
        related_name="products",  # user.products.all()
        null=True,
        blank=True,
    )

    is_published = models.BooleanField(
        default=False,
        verbose_name="Опубликовано",
    )

    def __str__(self):
        """Строковое представление объекта (для админки, shell)."""
        return self.name

    class Meta:
        """Метаданные модели (настройки таблицы БД)."""

        verbose_name = "продукт"  # Имя в единственном числе.
        verbose_name_plural = "продукты"  # Имя во множественном числе.
        ordering = ["-created_at"]  # Сортировка от новых к старым.

        # Добавим кастомное право изменять поле публикации.
        permissions = [
            ("can_unpublish_product", "Can unpublish product"),
        ]
