
from rest_framework import status
from rest_framework.test import APITestCase
from liberator.factories import *


class TestContent(APITestCase):
    def setUp(self):
        super(TestContent, self).setUp()
        self.admin = AdminFactory()
        self.admin.save()

        self.client.force_authenticate(user=self.admin)
        self.language = LanguageFactory()
        self.language.save()

        self.article = ArticleFactory()
        self.article.save()
        self.state = StateFactory()
        self.state.save()
        self.content = ContentFactory(
            article=self.article,
            language=self.language,
            author=self.admin,
            state=self.state
        )
        self.content.save()

    def test_article_revsions(self):
        url = "/api/v1/articles/%d/languages/%d/" % (
            self.article.pk,
            self.language.pk
        )
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertGreater(len(response.data), 0)

    def test_article_latest(self):
        url = "/api/v1/articles/%d/languages/latest/" % self.article.pk
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertGreater(len(response.data), 0)

    def test_content_list(self):
        url = "/api/v1/contents/"
        response = self.client.get(url)
        self.assertGreater(len(response.data), 0)

    def test_content_create(self):
        request = {
            "article": self.article.pk,
            "language": self.language.pk,
            "author": self.admin.pk,
            "title": "Some title",
            "text": "some text",
            "state": self.state.pk,
        }
        url = "/api/v1/contents/"
        response = self.client.post(url, request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_content_get(self):
        url = "/api/v1/contents/%d/" % self.content.pk
        response = self.client.get(url)
        self.assertEqual(response.data["id"], self.content.pk)

    def test_content_update(self):
        request = {
            "article": self.article.pk,
            "language": self.language.pk,
            "author": self.admin.pk,
            "title": "Some title",
            "text": "some text 1",
            "state": self.state.pk,
        }
        url = "/api/v1/contents/%d/" % self.content.pk
        response = self.client.put(url, request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["id"], self.content.pk)
