from rest_framework import serializers
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    nickname = serializers.CharField(source='nickname_id', read_only=True)

    class Meta:
        model = Comment
        fields = ['content', 'nickname']
        read_only_fields = ['nickname', 'board']

    def create(self, validated_data):
        # 현재 로그인한 사용자를 작성자로 설정
        user = self.context['request'].user

        # 사용자의 닉네임을 가져와서 할당
        validated_data['nickname'] = user.id_nickname

        return super().create(validated_data)