from django.urls import path

from board.views import BoardList, BoardDetail, MyBoardsView

urlpatterns = [
    path('boards/', BoardList.as_view(), name='board-list'),
    path('boards/post/', BoardDetail.as_view(), name='board-create'),
    path('boards/get/<int:pk>/', BoardDetail.as_view(), name='board-auth-list'),
    path('boards/put/<int:pk>/', BoardDetail.as_view(), name='board-update'),
    path('boards/delete/<int:pk>/', BoardDetail.as_view(), name='board-delete'),
    path('mypage/myboards', MyBoardsView.as_view(), name='my-boards'),
]
