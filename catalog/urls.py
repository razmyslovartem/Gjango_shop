from django.urls import path
from . import views


# Задаем пространство имен в файле маршрутизации приложения.
app_name = "catalog"

urlpatterns = [
    path("", views.home, name="home"),  # 127.0.0.1:8000/
    path("contacts/", views.contacts, name="contacts"),  # 127.0.0.1:8000/contacts/
    path("contact/", views.contacts, name="contact"),  # 127.0.0.1:8000/contact/
]
