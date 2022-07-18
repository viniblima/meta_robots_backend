from django.urls import path
from . import views

urlpatterns = [
    path('', views.RequestJoinTeamView.as_view(), name='create-request'),
    path('authorize/', views.AuthorizeJoinTeam.as_view(), name='authorize-request')
]
