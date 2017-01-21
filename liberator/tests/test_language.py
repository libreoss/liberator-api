
from rest_framework import status
from rest_framework.test import APITestCase
from liberator.factories import *


class TestLanguage(APITestCase):
    def setUp(self):
        super(TestLanguage, self).setUp()
        self.admin = AdminFactory()
        self.admin.save()

        self.client.force_authenticate(user=self.admin)

        self.article = ArticleFactory()
        self.article.save()

        self.language = LanguageFactory()
        self.language.save()

    def test_language_list(self):
        response = self.client.get("/api/v1/languages/")
        self.assertGreater(len(response.data), 0)

    def test_language_create(self):
        request = {
            "name": "some random language",
        }
        url = "/api/v1/languages/"
        response = self.client.post(url, request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_language_get(self):
        url = "/api/v1/languages/%d/" % self.language.pk
        response = self.client.get(url)
        self.assertEqual(response.data["id"], self.language.pk)

    def test_language_delete(self):
        url = "/api/v1/languages/%d/" % self.language.pk
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 204)
