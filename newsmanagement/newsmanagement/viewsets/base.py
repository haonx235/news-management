from rest_framework import viewsets

from ..models import BaseModel
from ..serializers import BaseSerializer


class BaseViewSet(viewsets.ModelViewSet):
    queryset = BaseModel.objects.all()
    serializer_class = BaseSerializer
