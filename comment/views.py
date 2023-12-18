from django.http import JsonResponse
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from comment.models import Comment
from comment.serializer import CommentSerializer, CommentCreateSerializer


class CommentListCreateView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentCreateAPIView(APIView):
    def post(self, request, board_id):
        # 댓글 작성 시 board_id를 context에 추가
        serializer = CommentCreateSerializer(data=request.data, context={'board_id': board_id})

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return JsonResponse({'message': '글이 존재하지 않습니다.'})

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)