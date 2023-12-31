from rest_framework import serializers

from board.models import Board
from report.models import Report
from tag.serializer import TagSerializer
from user.models import User


class BoardSerializer(serializers.ModelSerializer): # board post
    tags = TagSerializer(many=True, read_only=True)

    class Meta:
        model = Board
        fields = '__all__'
        read_only_fields = ['dt_created', 'dt_modified', 'author', 'nickname_author']

    def create(self, validated_data):
        # 현재 로그인한 사용자를 작성자로 설정
        user = self.context['request'].user

        # 사용자의 이메일을 가져와서 해당 이메일에 해당하는 사용자를 찾아 할당
        validated_data['author'] = User.objects.get(email=user.email)

        # 사용자의 닉네임을 가져와서 할당
        validated_data['nickname_author'] = user.id_nickname

        return super().create(validated_data)


class MyBoardsSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='board-detail')

    class Meta:
        model = Board
        fields = ['id', 'title', 'dt_created', 'dt_modified', 'url']
        read_only_fields = ['id', 'dt_created', 'dt_modified', 'url']


class ReportSerializer(serializers.ModelSerializer):
    board_url = serializers.HyperlinkedIdentityField(view_name='board-detail', source='board', read_only=True)

    class Meta:
        model = Report
        fields = ['id', 'reporter', 'board', 'board_url']
        read_only_fields = ['id', 'reporter', 'board', 'board_url']


class BoardNotLoginSerializer(serializers.ModelSerializer): #board get
    class Meta:
        model = Board
        fields = ['id', 'title', 'dt_created', 'dt_modified', 'nickname_author']
        read_only_fields = ['id', 'dt_created', 'dt_modified', 'nickname_author', 'author']


class BoardLoginSerializer(serializers.ModelSerializer): #board get
    tags = TagSerializer(many=True, read_only=True)  

    class Meta:
        model = Board
        fields = ['id', 'title', 'content', 'dt_created', 'dt_modified', 'nickname_author', 'comments', 'tags']
        read_only_fields = ['id', 'dt_created', 'dt_modified', 'nickname_author', 'author', 'comments']
