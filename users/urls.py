from django.urls import path, include
from users.views import register

urlpatterns = [
  path("accounts/", include("django.contrib.auth.urls")),
  path("oauth/", include("social_django.urls")),
  path("register/", register, name="register"),
]