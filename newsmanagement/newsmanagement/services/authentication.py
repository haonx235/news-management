from django.contrib.auth.hashers import check_password
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import APIException

from ..models import User
from ..serializers import UserSerializer


def check_authentication(data):
    if 'email' not in data:
        raise APIException('Email was not provided')
    if 'password' not in data:
        raise APIException('Password was not provided')
    email = data['email']
    password = data['password']
    if email is None or password is None:
        raise APIException('Some field data must not be null')

    try:
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        raise APIException('Email has not been registered')
    else:
        if check_password(password, user.password):
            user_serializer = UserSerializer(user)

            token, created = Token.objects.get_or_create(user=user)
            results = user_serializer.data
            results['token'] = token.key
            return results
        else:
            raise APIException('Password is not correct')
