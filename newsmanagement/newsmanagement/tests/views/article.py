from unittest import TestCase

from django.urls import reverse
from rest_framework.test import APIRequestFactory, APIClient

from ...models import Article, User


class ArticleTests(TestCase):
    factory = APIRequestFactory()

    def test_favorite(self):
        user = User(id=1, email='example@email.com', username='example', fullname='Example',
                    password='pbkdf2_sha256$390000$Qlc6MS0BmNOhSIKAo9DW4K$WQY1KoGKPMAe8lZNtXNCreLLd4bX/egsJB//5BoNDSY=')
        user.save()
        Article.objects.create(id=1, title='Article title', body='Lorem ipsum dolor sit amet.', favourite_count=0)
        api_client = APIClient()
        url = reverse('articles-favorite', kwargs={'pk': 1})
        api_client.force_authenticate(user=user)
        response = api_client.post(url, data={})
        self.assertEqual(Article.objects.get(pk=1).favourite_count, 1)
        self.assertEqual(response.status_code, 200)

    def test_unfavorite(self):
        user = User(id=2, email='example2@email.com', username='example2', fullname='Example2',
                    password='pbkdf2_sha256$390000$Qlc6MS0BmNOhSIKAo9DW4K$WQY1KoGKPMAe8lZNtXNCreLLd4bX/egsJB//5BoNDSY=')
        user.save()
        Article.objects.create(id=2, title='Article title', body='Lorem ipsum dolor sit amet.', favourite_count=1)
        api_client = APIClient()
        url = reverse('articles-favorite', kwargs={'pk': 2})
        api_client.force_authenticate(user=user)
        response = api_client.delete(url)
        self.assertEqual(Article.objects.get(pk=2).favourite_count, 0)
        self.assertEqual(response.status_code, 200)

