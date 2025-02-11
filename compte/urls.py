from django.urls import path
from .views import SignupView, CustomLoginView, logout_view, check_username

app_name = "compte"
urlpatterns = [
    path("signup/", SignupView.as_view(), name="signup"),
    path("login/", CustomLoginView.as_view(), name="login"),
    path("logout/", logout_view, name="logout"),
    path("check-username/", check_username, name="check_username"),
]
