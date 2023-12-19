from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions, serializers

from board.models import Board
from report.models import Report
from report.serializer import ReportSerializer


class ReportCreateView(generics.CreateAPIView):
    serializer_class = ReportSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        board_id = self.kwargs.get('board_id')
        board = get_object_or_404(Board, pk=board_id)

        # 이미 신고한 경우 처리
        if Report.objects.filter(reporter=self.request.user, board=board).exists():
            raise serializers.ValidationError('이미 신고한 게시글입니다.')

        serializer.save(reporter=self.request.user, board=board)