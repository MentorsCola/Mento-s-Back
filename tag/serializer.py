from rest_framework import serializers
from .models import Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'tag_content', 'board_id']
        read_only_fields = ['board_id']

        def create(self, validated_data):
            # 현재 요청이 속한 게시글의 ID를 가져옴
            board_id = self.context['view'].kwargs.get('board_id')

            # validated_data에 'board_id' 필드를 추가하여 저장
            validated_data['board_id'] = board_id

            # 부모 클래스의 create 메서드 호출
            return super().create(validated_data)
