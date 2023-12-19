from django.shortcuts import get_object_or_404
from rest_framework import serializers, status
from rest_framework.decorators import action
from rest_framework.response import Response

from board.models import Board
from .models import Report


class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = ['board']
        read_only_fields = ['reporter', 'board']

    @action(detail=True, methods=['post'])
    def report_board(self, request, pk=None):
        # 현재 로그인한 사용자를 확인
        user = request.user

        # 게시글 확인
        board = get_object_or_404(Board, pk=pk)

        # 이미 신고한 경우 처리
        if Report.objects.filter(reporter=user, board=board).exists():
            return Response({'detail': '이미 신고한 게시글입니다.'}, status=status.HTTP_400_BAD_REQUEST)

        # 신고 시 필요한 추가 로직 수행 (예: 관리자에게 알림 등)

        return Response({'detail': '게시글이 신고되었습니다.'}, status=status.HTTP_201_CREATED)
