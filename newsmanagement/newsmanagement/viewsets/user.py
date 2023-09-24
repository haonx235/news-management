from rest_framework import status
from rest_framework.decorators import action
from rest_framework.exceptions import APIException
from rest_framework.response import Response

from .base import BaseViewSet
from ..models import User
from ..serializers import UserSerializer


class UserViewSet(BaseViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

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
            user.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
