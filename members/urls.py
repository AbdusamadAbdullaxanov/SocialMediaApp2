from django.urls import path
from .views import (
    register_user,
    login_user,
    logout_user,
    verify_user,
)

urlpatterns = [
    path("register/", register_user, name="register"),
    path("login/", login_user, name="login"),
    path("logout/", logout_user, name="logout"),
    path("verify/", verify_user, name="verify"),
]
