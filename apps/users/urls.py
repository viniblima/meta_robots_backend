from django.urls import path

from . import views

urlpatterns = [
    path('login/', views.Login.as_view(), name='login'),
    path('refresh-token/', views.RefreshToken.as_view(), name='refresh-token'),
    path('signup/', views.CreateUserApiView.as_view(), name='user'),
    path('confirm/', views.ConfirmUserApiView.as_view(), name='confirm'),
    path('to-confirm/', views.UserToConfirmListApiView.as_view(), name='to-confirm'),
]
