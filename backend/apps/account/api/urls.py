from django.urls import path
from . import views

app_name='account'

urlpatterns = [
    path("api/signup/", views.SignupAPIView.as_view(),
          name="signup"),
    path("api/login/", views.LoginAPIView.as_view(),
          name="login"),
]