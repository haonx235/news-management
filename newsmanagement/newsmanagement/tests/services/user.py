from datetime import datetime
from django.test import TestCase
from django.core.exceptions import ObjectDoesNotExist
from unittest.mock import patch
from django_mock_queries.query import MockSet, MockModel
from rest_framework.exceptions import APIException

from ...models import User
from ...services.user import delete_user


class UserTests(TestCase):
    users = MockSet()
    user_objects = patch('newsmanagement.models.user.User.objects', users)

    @user_objects
    def test_delete_user_exception(self):
        self.users.add(
            MockModel(id=1, created_at=datetime.strptime('2023-09-24 07:00:00', '%Y-%m-%d %H:%M:%S'),
                      updated_at=datetime.strptime('2023-09-24 07:00:00', '%Y-%m-%d %H:%M:%S'),
                      email='example@email.com', username='example', fullname='Example',
                      password='pbkdf2_sha256$390000$Qlc6MS0BmNOhSIKAo9DW4K$WQY1KoGKPMAe8lZNtXNCreLLd4bX/egsJB//5BoNDSY=')
        )

        with self.assertRaises(APIException) as context:
            delete_user(None, 2)
        self.assertEqual('Email was not provided', context.exception.detail)

        with self.assertRaises(ObjectDoesNotExist):
            with self.assertRaises(APIException) as context:
                delete_user('example2@email.com', 1)
            self.assertEqual('Email has not been registered', context.exception.detail)

        with self.assertRaises(APIException) as context:
            delete_user('example@email.com', 1)
        self.assertEqual('Cannot delete current logged user', context.exception.detail)

    def test_delete_user(self):
        User.objects.create(id=1, email='example@email.com', username='example', fullname='Example',
                            password='pbkdf2_sha256$390000$Qlc6MS0BmNOhSIKAo9DW4K$WQY1KoGKPMAe8lZNtXNCreLLd4bX/egsJB//5BoNDSY=')
        delete_user('example@email.com', 2)
        self.assertFalse(User.objects.filter(id=1).exists())

