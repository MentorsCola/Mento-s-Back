from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from board.models import Board
from .models import Tag
from .serializer import TagSerializer


class TagCreateView(APIView):
    def post(self, request, board_id):
        # 요청에서 태그 정보 추출
        tags = request.data.get('tags')

        # 게시글 확인
        board = get_object_or_404(Board, pk=board_id)

        # 태그 생성 또는 가져오기
        tag, created = Tag.objects.get_or_create(tags=tags)

        # 게시글에 태그 추가
        board.tags.add(tag)

        # 태그 시리얼라이저로 변환
        serializer = TagSerializer(tag)

        return Response(serializer.data, status=status.HTTP_201_CREATED)