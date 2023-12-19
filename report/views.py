from rest_framework import generics, permissions

from board.models import Board
from report.serializer import ReportSerializer


class ReportCreateView(generics.CreateAPIView):
    serializer_class = ReportSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        board_id = self.kwargs.get('board_id')
        board = Board.objects.get(pk=board_id)
        serializer.save(reporter=self.request.user, board=board)