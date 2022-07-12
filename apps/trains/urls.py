from django.urls import path
from . import views

urlpatterns = [
    path('', views.TrainRobot.as_view(), name='train-robot'),
]
