# catalog/urls.py
from django.urls import path

from .views import ContactTemplateView
from .views import ProductDetailView
from .views import ProductListView

# Задаем пространство имен в файле маршрутизации приложения.
app_name = "catalog"

urlpatterns = [
    path("", ProductListView.as_view(), name="catalog_list"),
    path("product/<int:pk>/", ProductDetailView.as_view(), name="catalog_detail"),
    path("contacts/", ContactTemplateView.as_view(), name="contact"),
]
