from rest_framework import serializers
from .models import Report


class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = ['board']
        read_only_fields = ['reporter', 'board']

    def create(self, validated_data):
        # 현재 로그인한 사용자를 작성자로 설정
        user = self.context['request'].user

        return super().create(user)