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
        board = Board.objects.create(author=user, **validated_data)

        # 닉네임을 자동으로 할당 (랜덤으로 선택)
        all_nicknames = Nicknames.objects.all()
        if all_nicknames:
            random_nickname = random.choice(all_nicknames)
            board.nickname_author = random_nickname
            board.save()

        return board