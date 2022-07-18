from django.urls import path
from . import views

urlpatterns = [
    path('', views.TeamView.as_view(), name='create-team'),
    path('all/', views.ListTeamView.as_view(), name='get-all-teams'),
]
