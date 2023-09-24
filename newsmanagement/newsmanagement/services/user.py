from rest_framework.exceptions import APIException

from ..models import User


def delete_user(email, current_user_id):
    if email is None:
        raise APIException('Email was not provided')
    try:
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        raise APIException('Email has not been registered')
    else:
        if user.id == current_user_id:
            raise APIException('Cannot delete current logged user')
        user.delete()
