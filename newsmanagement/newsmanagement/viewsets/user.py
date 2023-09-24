from rest_framework import status, permissions
from rest_framework.decorators import action
from rest_framework.exceptions import APIException
from rest_framework.response import Response

from .base import BaseViewSet
from ..models import User
from ..serializers import UserSerializer


class UserViewSet(BaseViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.request.method == 'POST':
            return [permissions.AllowAny()]
        else:
            return super().get_permissions()

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset().exclude(pk=request.user.pk))

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(methods=['DELETE'], detail=False,
            url_path=r'(?P<email>\w+([.-]?\w+)*@\w+([.-]?\w+)*(\.\w{2,3})+)', url_name='delete_user')
    def delete_user(self, request, email=None):
        if email is None:
            raise APIException('Email was not provided')
        try:
            user = User.objects.get_by_natural_key(email=email)
        except User.DoesNotExist:
            raise APIException('Email has not been registered')
        else:
            if user.pk == request.user.pk:
                raise APIException('Cannot delete current logged user')
            user.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
