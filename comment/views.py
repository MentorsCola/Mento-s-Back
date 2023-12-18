from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import Comment
from board.models import Board  # Board 모델을 불러와야 합니다.
from .serializer import CommentSerializer


class CommentListCreateView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def create(self, request, *args, **kwargs):
        board_id = kwargs.get('board_id')
        board = Board.objects.get(pk=board_id)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(board=board)

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
