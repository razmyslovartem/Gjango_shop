# config/settings.py

import os
from pathlib import Path

from dotenv import load_dotenv

# Загружаем переменные окружения из файла .env
load_dotenv(override=True)

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/6.0/howto/deployment/checklist/

SECRET_KEY = os.getenv("SECRET_KEY")

DEBUG = True if os.getenv("DEBUG") == "True" else False

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    # Встроенные приложения.
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # Мои приложения.
    "django_bootstrap5",  # Стили по CDN.
    "django_extensions",  # Библиотека  django-extensions
    "catalog",  # Приложение 1
    "blog",  # Приложение 2
    "users",  # Приложение 3
]

AUTH_USER_MODEL = "users.User"  # Django для авторизации используй эту модель.

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",  # тип СУБД
        "NAME": os.getenv("DB_NAME"),  # имя базы данных
        "USER": os.getenv("DB_USER"),  # имя пользователя
        "PASSWORD": os.getenv("DB_PASSWORD"),  # пароль пользователя
        "HOST": os.getenv("DB_HOST"),  # адрес сервера базы данных
        "PORT": os.getenv("DB_PORT", default="5432"),  # порт, на котором работает PostgreSQL
    }
}


AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


LANGUAGE_CODE = "ru-RU"

TIME_ZONE = "Europe/Moscow"

USE_I18N = True

USE_L10N = False  # отключает локализованное форматирование дат, чисел и времени.

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/6.0/howto/static-files/

STATIC_URL = "static/"
STATICFILES_DIRS = [BASE_DIR / "static"]  # Папка со статическими файлами (CSS, JS, изображения для сайта)
STATIC_ROOT = BASE_DIR / "staticfiles"  # Папка, куда собираются все статические файлы для продакшена

# MEDIA файлы (загрузки пользователей)
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Настройки почты (для разработки - вывод в консоль)
# EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
# DEFAULT_FROM_EMAIL = "noreply@djangoshop.ru"

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
# Вариант Console backend (письма будут выводиться в терминал)
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Для реальной отправки:
EMAIL_HOST = "smtp.yandex.ru"  # Хост Яндекса
EMAIL_PORT = 465  # Для SSL
EMAIL_USE_SSL = True  # Для SSL
EMAIL_USE_TLS = False  # При SSL TLS не используется
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER")  # Ваш реальный логин
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD")  # Пароль от почты или пароль приложения

LOGIN_URL = "users:login"
# Редирект для перенаправлений после входа и выхода.
LOGIN_REDIRECT_URL = "catalog:product_list"
LOGOUT_REDIRECT_URL = "catalog:product_list"
