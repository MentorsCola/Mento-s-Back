from os import path

from comment.views import CommentCreateAPIView, CommentListCreateView

urlpatterns = [
    path('comments/create/<int:board_id>/', CommentCreateAPIView.as_view(), name='comment-create'),
    path('comments/', CommentListCreateView.as_view(), name='comment-create'),
]