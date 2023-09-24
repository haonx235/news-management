from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework import mixins, status
from rest_framework.decorators import action
from rest_framework.exceptions import APIException
from rest_framework.generics import UpdateAPIView
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

from .base import BaseViewSet
from ..models import Article
from ..serializers import ArticleSerializer


@extend_schema_view(
    create=extend_schema(
        operation={
            "operationId": "api_articles_create",
            "tags": ["api"],
            "parameters": [{
                "in": "header",
                "name": "Authorization",
                "schema": {"type": "string"},
                "description": "Authorization token"
            }],
            "requestBody": {
                "content": {
                    "application/json": {
                        "schema": {
                            "type": "object",
                            "properties": {
                                "title": {"type": "string"},
                                "body": {"type": "string", "description": "Article description"}
                            }
                        }
                    },
                }
            },
            "responses": {
                "201": {
                    "content": {
                        "application/json": {
                            "schema": {
                                "$ref": "#/components/schemas/Article"
                            }
                        }
                    },
                    "description": ""
                },
            }
        }
    ),
    update=extend_schema(
        operation={
            "operationId": "api_articles_update",
            "tags": ["api"],
            "parameters": [
                {
                    "in": "header",
                    "name": "Authorization",
                    "schema": {"type": "string"},
                    "description": "Authorization token"
                },
                {
                    "in": "path",
                    "name": "id",
                    "schema": {"type": "integer"},
                    "description": "A unique integer value identifying this article.",
                    "required": "true"
                }
            ],
            "requestBody": {
                "content": {
                    "application/json": {
                        "schema": {
                            "type": "object",
                            "properties": {
                                "title": {"type": "string"},
                                "body": {"type": "string", "description": "Article description"}
                            }
                        }
                    },
                }
            },
            "responses": {
                "200": {
                    "content": {
                        "application/json": {
                            "schema": {
                                "$ref": "#/components/schemas/Article"
                            }
                        }
                    },
                    "description": ""
                },
            }
        }
    ),
)
class ArticleViewSet(BaseViewSet,
                     UpdateAPIView,
                     mixins.DestroyModelMixin):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'title']
    http_method_names = ["get", "post", "put", "delete"]

    @extend_schema(methods=["post", "delete"], operation={
        "operationId": "api_articles_favorite_unfavorite",
        "description": "Favorite/Unfavorite article (POST for favorite, DELETE for unfavorite)",
        "tags": ["api"],
        "parameters": [
            {
                "in": "header",
                "name": "Authorization",
                "schema": {"type": "string"},
                "description": "Authorization token"
            },
            {
                "in": "path",
                "name": "id",
                "schema": {"type": "integer"},
                "description": "A unique integer value identifying this article.",
                "required": "true"
            }
        ],
        "responses": {
            "200": {
                "content": {
                    "application/json": {
                        "schema": {
                            "$ref": "#/components/schemas/Article"
                        }
                    }
                },
                "description": ""
            },
        }
    })
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
