from rest_framework import serializers

from ..models import BaseModel


class BaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseModel
        fields = ['id', 'created_at', 'updated_at']
        abstract = True
