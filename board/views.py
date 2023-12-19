from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework import permissions, status, generics
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from comment.models import Comment
from comment.serializer import CommentSerializer
from .BoardSerializer import BoardSerializer, BoardNotLoginSerializer, BoardLoginSerializer, MyBoardsSerializer
from .models import Board


class BoardList(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        boards = Board.objects.all()
        serializer = BoardNotLoginSerializer(boards, many=True)
        return Response({'boards': serializer.data}, status=status.HTTP_200_OK)

class SortBoard(APIView):
    # permission_classes = [permissions.AllowAny]
    
    def get(self, request):
        boards = Board.objects.all()
        serializer = BoardNotLoginSerializer(boards, many=True)
        board_list =[]

        for i in serializer.data:
            n_board = get_object_or_404(Board, pk=i['id'])
            a_board = {
                'id': i['id'],
                'title': i['title'],
                'dt_created': i['dt_created'],
                'dt_modified': i['dt_modified'],
                'nickname_author': i['nickname_author'],
                'likes':n_board.like.count()
            }
            check = False
            for j in range(0, len(board_list)):
                if(board_list[j]['likes']>a_board['likes']):
                    board_list.insert(j, a_board)
                    check=True
                    break
            
            if(check==False):
                board_list.append(a_board)
        board_list.reverse()
        return Response({'boards': board_list}, status=status.HTTP_200_OK)

@permission_classes([permissions.IsAuthenticated])
class MyBoardsView(generics.ListAPIView):
    serializer_class = MyBoardsSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # 현재 로그인한 사용자의 글만 조회
        return Board.objects.filter(author=self.request.user)


@permission_classes([permissions.IsAuthenticated])
class BoardDetail(generics.RetrieveAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardLoginSerializer

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        comments = Comment.objects.filter(board=instance)
        comments_serializer = CommentSerializer(comments, many=True)
        data = serializer.data
        data['comments'] = comments_serializer.data
        return Response(data)

    def post(self, request):
        serializer = BoardSerializer(data=request.data, context={'request': request})  # context에 request를 명시적으로 전달

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        board = get_object_or_404(Board, pk=pk)
        self.check_object_permissions(request, board)

        serializer = BoardSerializer(board, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'message': '글이 성공적으로 수정되었습니다.'})
        return JsonResponse({'error': serializer.errors}, status=400)

    def delete(self, request, pk):
        board = get_object_or_404(Board, pk=pk)
        self.check_object_permissions(request, board)
        board.delete()
        return JsonResponse({'message': '글이 성공적으로 삭제되었습니다.'})