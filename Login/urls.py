from django.urls import path
from .views import UserRegisterView

from . import views

app_name = "Login"

urlpatterns = [
    path('', UserRegisterView.as_view(), name='register'),
]