from django.urls import path
from . import views

urlpatterns = [
    path('', views.CreateRobot.as_view(), name='create-robot'),
]
