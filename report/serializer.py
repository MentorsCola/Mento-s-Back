from django.shortcuts import get_object_or_404
from rest_framework import serializers, status
from rest_framework.decorators import action
from rest_framework.response import Response

from board.models import Board
from .models import Report


class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = '__all__'
        read_only_fields = ['reporter', 'board']

    @action(detail=True, methods=['post'])
    def report_board(self, request, pk=None):
        # 현재 로그인한 사용자를 확인
        user = request.user

        # 게시글 확인
        board = get_object_or_404(Board, pk=pk)

        # 이미 신고한 경우 처리
        if Report.objects.filter(reporter=user, board=board).exists():
            return Response({'message': '이미 신고한 게시글입니다.'}, status=status.HTTP_400_BAD_REQUEST)

        # 신고 생성
        report = Report.objects.create(reporter=user, board=board)

        return Response({'message': '게시글이 신고되었습니다.'}, status=status.HTTP_201_CREATED)