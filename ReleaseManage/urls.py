from django.urls import path

from . import views

app_name = 'ReleaseManage'

urlpatterns = [
    path('', views.release, name='release-home')
]