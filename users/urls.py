# users/urls.py

from django.urls import path

from .views import UserLoginView
from .views import UserLogoutView
from .views import UserRegisterView
from .views import email_verification

app_name = "users"


urlpatterns = [
    path("login/", UserLoginView.as_view(), name="login"),
    path("logout/", UserLogoutView.as_view(), name="logout"),
    path("register/", UserRegisterView.as_view(), name="register"),
    path("email-confirm/<str:token>/", email_verification, name="email_confirm"),
]
