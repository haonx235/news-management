from rest_framework import serializers

from .base import BaseSerializer
from ..models import Article


class ArticleSerializer(BaseSerializer):
    # title = serializers.CharField(max_length=250, allow_blank=True)
    # body = serializers.CharField(allow_blank=True)
    # favourite_count = serializers.IntegerField(default=0)

    class Meta:
        model = Article
        fields = ['id', 'created_at', 'updated_at', 'title', 'body', 'favourite_count']

