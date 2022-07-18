from django.urls import path
from . import views

urlpatterns = [
    path('', views.CreateMatch.as_view(), name='create-match'),
]
