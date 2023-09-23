from django.contrib.auth.hashers import check_password
from rest_framework.decorators import api_view
from rest_framework.exceptions import APIException
from rest_framework.response import Response

from ..models import User
from ..serializers import UserSerializer


@api_view(['POST'])
def login(request):
    request_data = request.data.copy()
    if 'email' not in request_data:
        raise APIException('Email not found')
    if 'password' not in request_data:
        raise APIException('Password not found')
    email = request_data['email']
    password = request_data['password']
    if email is None or password is None:
        raise APIException('Some field data must not be null')

    try:
        user = User.objects.get_by_natural_key(email=email)
    except User.DoesNotExist:
        raise APIException('Email has not been registered')
    else:
        if check_password(password, user.password):
            user_serializer = UserSerializer(user)
            return Response(user_serializer.data)
        else:
            raise APIException('Password is not correct')
