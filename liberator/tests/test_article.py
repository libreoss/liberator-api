
from rest_framework import status
from rest_framework.test import APITestCase
from liberator.factories import (
    UserFactory,
    AdminFactory,
    ArticleFactory,
    IssueFactory
)


class TestArticle(APITestCase):
    def setUp(self):
        super(TestArticle, self).setUp()
        self.admin = AdminFactory()
        self.client.force_authenticate(user=self.admin)
        self.admin.save()
        self.article = ArticleFactory()
        self.article.save()
        self.issue = IssueFactory()

    def test_article_list(self):
        response = self.client.get("/api/v1/articles/")
        self.assertGreater(len(response.data), 0)

    def test_article_create(self):
        request = {
            "authors": [
                self.admin.pk
            ],
        }
        url = "/api/v1/articles/"
        response = self.client.post(url, request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_article_create_with_issues(self):
        request = {
            "authors": [
                self.admin.pk
            ],
            "issues": [
                self.issue.pk
            ]
        }
        url = "/api/v1/articles/"
        response = self.client.post(url, request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertGreater(len(response.data["issues"]), 0)

    def test_article_get(self):
        url = "/api/v1/articles/%d/" % self.article.pk
        response = self.client.get(url)
        self.assertEqual(response.data["id"], self.article.pk)

    def test_article_update(self):
        request = {
            "authors": [
                self.admin.pk,
            ],
        }
        url = "/api/v1/articles/%d/" % self.article.pk
        response = self.client.put(url, request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["id"], self.article.pk)

    def test_article_delete(self):
        url = "/api/v1/articles/%d/" % self.article.pk
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 204)
