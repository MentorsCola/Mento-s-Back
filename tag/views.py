from rest_framework.response import Response
from rest_framework.views import APIView

from board.models import Board
from tag.models import Tag
from tag.serializer import TagSerializer


class TagCreateView(APIView):
    def post(self, request, board_id):
    # 요청에서 태그 정보 추출
        tag_content = request.data.get('tag_content')

    # 게시글 확인
        board = Board.objects.get(pk=board_id)

    # 태그 생성
        tag = Tag.objects.create(board=board, tag_content=tag_content)

    # 태그 시리얼라이저로 변환
        serializer = TagSerializer(tag)

        return Response(serializer.data, status=status.HTTP_201_CREATED)