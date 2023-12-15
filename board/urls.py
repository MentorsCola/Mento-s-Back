from django.urls import path

from board.views import BoardList, BoardDetail

urlpatterns = [
    path('boards/', BoardList.as_view(), name='board-list'),
    path('boards/post/', BoardDetail.as_view(), name='board-create'),
    path('boards/get/<int:pk>/', BoardDetail.as_view(), name='board-auth-list'),
    path('boards/put/', BoardDetail.as_view(), name='board-update'),
    path('boards/delete/', BoardDetail.as_view(), name='board-delete'),
]
