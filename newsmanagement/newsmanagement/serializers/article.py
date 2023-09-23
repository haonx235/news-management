from rest_framework import serializers

from .base import BaseSerializer
from ..models import Article


class ArticleSerializer(BaseSerializer):

    class Meta:
        model = Article
        fields = ['id', 'created_at', 'updated_at', 'title', 'body', 'favourite_count']

