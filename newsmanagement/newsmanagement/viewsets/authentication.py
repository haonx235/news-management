from django.contrib.auth.hashers import check_password
from rest_framework.decorators import api_view, permission_classes
from rest_framework.exceptions import APIException
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from ..models import User
from ..serializers import UserSerializer


@api_view(['POST'])
@permission_classes([])
def login(request):
    request_data = request.data.copy()
    if 'email' not in request_data:
        raise APIException('Email was not provided')
    if 'password' not in request_data:
        raise APIException('Password was not provided')
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

            token, created = Token.objects.get_or_create(user=user)
            results = user_serializer.data
            results['token'] = token.key
            return Response(results)
        else:
            raise APIException('Password is not correct')
