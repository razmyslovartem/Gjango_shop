# Gjango-shop

Проект интернет-магазина на Django.

## Технологии
- Python 3.14
- Django 6.06
- Poetry (управление зависимостями)
- Bootstrap 5 (вёрстка)
- PostgreSQL (база данных)

## Установка

```bash
# Клонирование
git clone <url>
cd Gjango-shop

# Установка зависимостей
poetry install

# Активация окружения
poetry shell

# Миграции БД
poetry run python manage.py migrate

# Запуск сервера
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