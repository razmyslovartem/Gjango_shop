# Gjango-shop

Проект интернет-магазина на Django.

## Технологии
- Python 3.14
- Django 6.06
- Poetry (управление зависимостями)
- Bootstrap 5 (вёрстка)

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
├── catalog/ # Приложение каталога
├── templates/ # HTML-шаблоны
├── sky_shop/ # Настройки проекта
└── manage.py
```

## Приложения
- **catalog/** — каталог товаров, контакты

## Адреса
- Главная: http://127.0.0.1:8000/
- Контакты: http://127.0.0.1:8000/contacts/
