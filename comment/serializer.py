from rest_framework import serializers

from comment.models import Comment


class CommentSerializer(serializers.ModelSerializer): # 댓글 조회
    class Meta:
        model = Comment
        fields = '__all__'


class CommentCreateSerializer(serializers.ModelSerializer): # comment post
    nickname_commend = serializers.ReadOnlyField(source='nickname_commend.nickname')  # 닉네임을 읽기 전용 필드로 설정

    class Meta:
        model = Comment
        fields = ['content', 'nickname_commend']

    def create(self, validated_data):
        # 댓글을 작성한 글의 ID를 가져오기
        board_id = self.context['board_id']

        # 댓글 생성
        comment = Comment.objects.create(
            content=validated_data['content'],
            board_id=board_id,
            nickname_commend=validated_data.get('nickname_commend')
        )

        return comment