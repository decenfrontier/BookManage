from rest_framework import serializers

from book.models import BookInfo


class PeopleSerializer(serializers.Serializer):
    name = serializers.CharField()
    description = serializers.CharField()
    book = serializers.StringRelatedField()

class BookSerializer(serializers.Serializer):
    name = serializers.CharField()
    pub_date = serializers.DateField(read_only=True)
    readcount = serializers.IntegerField()
    commentcount = serializers.IntegerField(default=0)
    peopleinfo_set = PeopleSerializer(many=True, read_only=True)  # 返回自定义的人物信息

    def validate_name(self, value):
        """单一字段验证, 固定写法"""
        if value == 'python':
            raise serializers.ValidationError('书名不能是python')
        return value

    def validate(self, attrs):
        """多个字段验证, 固定写法"""
        if attrs['commentcount'] > attrs['readcount']:
            raise serializers.ValidationError('评论量大于阅读量')
        return attrs

    def create(self, validated_data):
        return BookInfo.objects.create(**validated_data)