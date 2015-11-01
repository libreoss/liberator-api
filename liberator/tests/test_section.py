
from rest_framework import status 
from rest_framework.test import APITestCase
from liberator.factories import *

class TestSection(APITestCase):
    def setUp(self):
        super(TestSection, self).setUp()
        self.admin = AdminFactory()
        self.admin.save()

        self.client.force_authenticate(user=self.admin)
        
        self.section = SectionFactory()
        self.section.save()

        self.article = ArticleFactory(section=self.section)
        self.article.save()

    def test_section_list(self):
        response = self.client.get("/api/v1/sections/")
        self.assertGreater(len(response.data), 0)
    
    def test_section_create(self):
        request = {
            "name": "some random section",
        }
        url = "/api/v1/sections/"
        response = self.client.post(url, request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_section_get(self):
        url = "/api/v1/sections/%d/" % self.section.pk
        response = self.client.get(url)
        self.assertEqual(response.data["id"], self.section.pk)
 
    def test_section_delete(self):
        url = "/api/v1/sections/%d/" % self.section.pk
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 204)

    def test_section_article_list(self):
        response = self.client.get("/api/v1/sections/%d/articles/" % self.section.pk)
        self.assertGreater(len(response.data), 0)
