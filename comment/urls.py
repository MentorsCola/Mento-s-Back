
from django.urls import path
from .views import CommentListCreateView

urlpatterns = [
    path('comments/<int:board_id>/', CommentListCreateView.as_view(), name='comment-list-create'),
]