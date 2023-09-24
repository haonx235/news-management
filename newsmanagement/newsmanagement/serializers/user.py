from drf_spectacular.utils import extend_schema_serializer

from .base import BaseSerializer
from ..models import User


@extend_schema_serializer(
    exclude_fields=['password']
)
class UserSerializer(BaseSerializer):

    class Meta:
        model = User
        fields = ['id', 'created_at', 'updated_at', 'email', 'username', 'fullname', 'password']

    def to_representation(self, instance):
        return {
            'id': instance.pk,
            'created_at': instance.created_at,
            'updated_at': instance.updated_at,
            'email': instance.email,
            'username': instance.username,
            'fullname': instance.fullname
        }