from django.urls import path

from board.views import BoardList, BoardDetail, MyBoardsView, LikeBoard, MyReportView

urlpatterns = [
    path('boards/', BoardList.as_view(), name='board-list'),
    path('like/', LikeBoard.as_view(), name='board-likes'),
    path('boards/post/', BoardDetail.as_view(), name='board-create'),
    path('boards/get/<int:pk>/', BoardDetail.as_view(), name='board-detail'),
    path('boards/put/<int:pk>/', BoardDetail.as_view(), name='board-detail'),
    path('boards/delete/<int:pk>/', BoardDetail.as_view(), name='board-detail'),
    path('mypage/myboards/', MyBoardsView.as_view(), name='my-boards'),
    path('mypage/myreport/', MyReportView.as_view(), name='my-reports'),
]
