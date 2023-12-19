from rest_framework import serializers

from tag.models import Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'board', 'tag_content']
        read_only_fields = ['id', 'board']

