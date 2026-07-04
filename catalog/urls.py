# catalog/urls.py
from django.urls import path

from . import views

# Задаем пространство имен в файле маршрутизации приложения.
app_name = "catalog"

urlpatterns = [
    path("", views.catalog_list, name="catalog_list"),
    path("product/<int:pk>/", views.catalog_detail, name="catalog_detail"),
    path("contacts/", views.contacts, name="contacts"),  # GET - показать форму
    path("contact/", views.contact, name="contact"),  # POST - обработать форму
]
