# blog/urls.py

from django.urls import path

from .views import BlogPostCreateView
from .views import BlogPostDeleteView
from .views import BlogPostDetailView
from .views import BlogPostListView
from .views import BlogPostUpdateView

app_name = "blog"


urlpatterns = [
    path("", BlogPostListView.as_view(), name="list"),
    path("<int:pk>/", BlogPostDetailView.as_view(), name="detail"),
    path("create/", BlogPostCreateView.as_view(), name="create"),
    path("<int:pk>/update/", BlogPostUpdateView.as_view(), name="update"),
    path("<int:pk>/delete/", BlogPostDeleteView.as_view(), name="delete"),
]
