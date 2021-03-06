from django.urls import path, include
from .views import UserEditView
from django.contrib.auth import views as auth_views

from . import views

app_name = "Login"

urlpatterns = [
  
    path('edit_profile/', UserEditView.as_view(), name='edit_profile'),
    path('password/', auth_views.PasswordChangeView.as_view()),
]
