from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from user.views import UserListView, RegisterAPIView, AuthAPIView

urlpatterns = [
    path('register/', RegisterAPIView.as_view(), name='user-register'),
    path('users/', UserListView.as_view(), name='user-list'), #allowAnyone
    path('users/', AuthAPIView.as_view(), name='user-list, user-login, logout'),
    path('auth/refresh/', TokenRefreshView.as_view()), # jwt 토큰 재발급
]