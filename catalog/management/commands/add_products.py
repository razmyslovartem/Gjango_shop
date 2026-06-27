"""
Кастомная команда для загрузки тестовых данных в БД.
Команда удаляет все существующие категории и продукты,
затем создаёт новые тестовые данные для разработки и тестирования.
Для использования команда: poetry run python manage.py add_products
"""

from django.core.management.base import BaseCommand
from catalog.models import Category, Product


class Command(BaseCommand):
    """Создание класса для нашей команды"""
    help = 'Обнуляет БД и записывает тестовые данные в БД.'  #  Атрибут help описывает что делает команда.

    #  В методе handle описан основной код(логика) нашей команды(макроса).
    def handle(self, *args, **kwargs):

        # 1. Удаляем существующие данные.
        Product.objects.all().delete()
        Category.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('Данные очищены!'))

        # 2 Создаём категории
        self.stdout.write(self.style.WARNING('Создание категорий...'))

        electronics = Category.objects.create(
            name='Электроника',
            description='Гаджеты и техника'
        )

        clothing = Category.objects.create(
            name='Одежда',
            description='Одежда и модные аксессуары'
        )

        books = Category.objects.create(
            name='Книги',
            description='Художественная и учебная литература'
        )

        sport = Category.objects.create(
            name='Спорт',
            description='Спортивные товары и инвентарь'
        )

        self.stdout.write(self.style.SUCCESS(f'Создано {Category.objects.count()} категорий'))

        # 3. Создаём продукты
        self.stdout.write(self.style.WARNING('Создание продуктов...'))

        products = [
            {
                'name': 'iPhone 15',
                'description': 'Смартфон Apple',
                'image': '',
                'category': electronics,
                'price': 115000.00
            },
            {
                'name': 'MacBook Pro',
                'description': 'Ноутбук Apple',
                'image': '',
                'category': electronics,
                'price': 250000.00
            },
            {
                'name': 'Трико',
                'description': 'Классические штаны',
                'image': '',
                'category': clothing,
                'price': 500.00
            },
            {
                'name': 'Куртка Nike',
                'description': 'Спортивная куртка',
                'image': '',
                'category': clothing,
                'price': 12000.00
            },
            {
                'name': 'Футбольный мяч',
                'description': 'Кожаный мяч',
                'image': '',
                'category': sport,
                'price': 2999.00
            },
        ]

    # Добавляем продукты через цикл с проверкой.
        for product_data in products:
            # Используем get_or_create для избежания дубликатов
            product, created = Product.objects.get_or_create(**product_data)

            if created:
                self.stdout.write(
                    self.style.SUCCESS(f'Добавлен продукт: {product.name} - {product.price} руб.')
                )
            else:
                self.stdout.write(
                    self.style.WARNING(f'Продукт уже существует: {product.name}')
                )

        self.stdout.write(self.style.SUCCESS(f'\nВсего обработано: {len(products)} продуктов'))