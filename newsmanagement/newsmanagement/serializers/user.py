from rest_framework import serializers

from .base import BaseSerializer
from ..models import User


class UserSerializer(BaseSerializer):
    # email = serializers.CharField(max_length=255, allow_blank=False)
    # username = serializers.CharField(max_length=255, allow_blank=False)
    # fullname = serializers.CharField(max_length=128, allow_blank=False)
    # password = serializers.CharField(allow_blank=False)

    class Meta:
        model = User
        fields = ['id', 'created_at', 'updated_at', 'email', 'username', 'fullname']
