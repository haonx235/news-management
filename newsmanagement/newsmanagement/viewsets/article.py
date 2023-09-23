from rest_framework import mixins, status
from rest_framework.decorators import action
from rest_framework.exceptions import APIException
from rest_framework.response import Response

from .base import BaseViewSet
from ..models import Article
from ..serializers import ArticleSerializer


class ArticleViewSet(BaseViewSet,
                     mixins.UpdateModelMixin):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    @action(methods=['POST', 'DELETE'], detail=True, url_path='favorite', url_name='favorite')
    def favorite(self, request, pk):
        if self.request.method == 'POST':
            article = self.get_object()
            article.favourite_count += 1
            article.save()
            article_serializer = ArticleSerializer(article)
            return Response(article_serializer.data, status=status.HTTP_200_OK)
        elif self.request.method == 'DELETE':
            article = self.get_object()
            if article.favourite_count > 0:
                article.favourite_count -= 1
                article.save()
                article_serializer = ArticleSerializer(article)
                return Response(article_serializer.data, status=status.HTTP_200_OK)
            else:
                raise APIException(detail='Favourite count of this article is zero')
