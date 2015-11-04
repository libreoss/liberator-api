
from rest_framework import status
from rest_framework.test import APITestCase
from liberator.factories import *

class TestComment(APITestCase):
    def setUp(self):
        super(TestComment, self).setUp()
        self.admin = AdminFactory()
        self.admin.save()

        self.client.force_authenticate(user=self.admin)
        
        self.article = ArticleFactory()
        self.article.save()

        self.comment = CommentFactory(article = self.article, author=self.admin) 
        self.comment.save()

    def test_comment_list(self):
        response = self.client.get("/api/v1/comments/")
        self.assertGreater(len(response.data), 0)

    def test_comment_create(self):
        request = {
            "article": article.pk,
            "author": self.admin.email,
            "text": "this is some comment", 
        }
        url = "/api/v1/comments/"
        response = self.client.post(url, request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_comment_get(self):
        url = "/api/v1/comment/%d/" % self.comment.pk
        response = self.client.get(url)
        self.assertEqual(response.data["id"], self.comment.pk)

    def test_comment_delete(self):
        url = "/api/v1/comments/%d/" % self.comment.pk
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 204)
