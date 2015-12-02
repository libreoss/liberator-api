
from rest_framework import status 
from rest_framework.test import APITestCase
from liberator.factories import *

class TestIssue(APITestCase):
    def setUp(self):
        super(TestIssue, self).setUp()
        self.admin = AdminFactory()
        self.admin.save()

        self.client.force_authenticate(user=self.admin)

        self.article = ArticleFactory()
        self.article.save()
        
        self.issue = IssueFactory()
        self.issue.save()

        self.article.issues.add(self.issue)
        self.article.save()

    def test_issue_list(self):
        response = self.client.get("/api/v1/issues/")
        self.assertGreater(len(response.data), 0)
    
    def test_issue_create(self):
        request = {
            "name": "Issue 1",
            "special": False,
            "published": False,
        }
        url = "/api/v1/issues/"
        response = self.client.post(url, request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_issue_get(self):
        url = "/api/v1/issues/%d/" % self.issue.pk
        response = self.client.get(url)
        self.assertEqual(response.data["id"], self.issue.pk)
 
    def test_section_delete(self):
        url = "/api/v1/issues/%d/" % self.issue.pk
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 204)

    def test_issue_article_list(self):
        response = self.client.get("/api/v1/issues/%d/articles/" % self.issue.pk)
        self.assertEqual(response.status_code, 200)
        self.assertGreater(len(response.data), 0)
