from .base import BaseViewSet
from ..models import Article
from ..serializers import ArticleSerializer


class ArticleViewSet(BaseViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
