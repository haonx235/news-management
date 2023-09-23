from rest_framework import mixins, viewsets

from ..serializers import BaseSerializer


class BaseViewSet(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  mixins.DestroyModelMixin,
                  viewsets.GenericViewSet):
    serializer_class = BaseSerializer

    class Meta:
        abstract = True
