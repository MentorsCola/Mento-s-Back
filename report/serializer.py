from django.shortcuts import get_object_or_404
from rest_framework import serializers, status
from rest_framework.response import Response

from board.models import Board
from .models import Report


class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = '__all__'
        read_only_fields = ['reporter', 'board']

    def report_board(self, request):
        # 현재 로그인한 사용자를 확인
        user = request.user

        # 전달된 board_id를 가져오기
        board_id = request.data.get('board_id')

        # 게시글 확인
        board = get_object_or_404(Board, pk=board_id)

        return Response({'message': '게시글이 신고되었습니다.'}, status=status.HTTP_201_CREATED)