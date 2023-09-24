from datetime import datetime

from django.test import TestCase
from unittest.mock import patch
from django_mock_queries.query import MockSet, MockModel

from ...services.authentication import check_authentication


class AuthenticationTests(TestCase):
    users = MockSet()
    user_objects = patch('newsmanagement.models.user.User.objects', users)
    tokens = MockSet()
    token_objects = patch('rest_framework.authtoken.models.Token.objects', tokens)

    @user_objects
    @token_objects
    def test_check_authorization(self):
        mocked_user = MockModel(
            id=1, created_at=datetime.strptime('2023-09-24 07:00:00', '%Y-%m-%d %H:%M:%S'),
            updated_at=datetime.strptime('2023-09-24 07:00:00', '%Y-%m-%d %H:%M:%S'),
            email='example@email.com', username='example', fullname='Example',
            password='pbkdf2_sha256$390000$Qlc6MS0BmNOhSIKAo9DW4K$WQY1KoGKPMAe8lZNtXNCreLLd4bX/egsJB//5BoNDSY='
        )
        self.users.add(mocked_user)
        self.tokens.add(
            MockModel(user=mocked_user, created=datetime.strptime('2023-09-24 07:00:00', '%Y-%m-%d %H:%M:%S'),
                      key='ee812b8954f38cdf97024c3dca42557d4df93246')
        )
        results = check_authentication({'email': 'example@email.com', 'password': '123456'})
        self.assertEqual(results['username'], 'example')
        self.assertEqual(results['fullname'], 'Example')
