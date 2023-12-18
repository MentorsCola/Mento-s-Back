from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from nicknames.views import NicknameView

urlpatterns = [
    path('view/', NicknameView.as_view(), name='nickname-view')
]