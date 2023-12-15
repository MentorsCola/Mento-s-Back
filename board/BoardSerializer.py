import random

from rest_framework import serializers

from board.models import Board
from nicknames.models import Nicknames


class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = '__all__'
        read_only_fields = ['dt_created', 'dt_modified', 'author', 'nickname_author']

    def create(self, validated_data):
        # 현재 로그인한 사용자를 작성자로 설정
        user = self.context['request'].user

        # 사용자의 닉네임을 가져와서 할당
        validated_data['nickname_author'] = user.id_nickname

        return super().create(validated_data)