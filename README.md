# Gjango-shop

Проект интернет-магазина на Django с каталогом, блогом и пользователями.

## Технологии
- Python 3.13
- Django 5.1
- Poetry (управление зависимостями)
- Bootstrap 5 (frontend)
- PostgreSQL (база данных)
- Pillow (обработка изображений)

## Установка

```bash
# Клонирование репозитория
git clone <url>
cd Gjango-shop

# Установка зависимостей через Poetry
poetry install

# Активация виртуального окружения
poetry shell

# Миграции БД
poetry run python manage.py migrate

# Создание суперпользователя для админки
poetry run python manage.py createsuperuser

# Запуск сервера разработки
poetry run python manage.py runserver
```

## Структура

```markdown
Gjango-shop/
│   ├── management/
│   │   └── commands/
│   │       └── add_products.py # Кастомная команда загрузки данных
│   ├── fixtures/               # Фикстуры для тестовых данных
│   ├── models.py
│   └── views.py
├── templates/                  # HTML-шаблоны
├── config/                     # Настройки проекта
├── export_fixtures.py          # Скрипт экспорта в UTF-8
└── manage.py
```

## Приложения
- **catalog/** — каталог товаров, контакты

## Адреса
- Главная: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
- Каталог: [http://127.0.0.1:8000/catalog/](http://127.0.0.1:8000/catalog/)
- Контакты: [http://127.0.0.1:8000/contacts/](http://127.0.0.1:8000/contacts/)
- Админ-панель: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)