from django.conf.urls import url
from .views import RegisterView, LoginView, JwtView
from django.urls import path

urlpatterns = [
    path('register/', RegisterView.as_view(), name="register"),
    path('login/', LoginView.as_view(), name="login"),
    path('jwt/', JwtView.as_view(), name="jwt")
]
