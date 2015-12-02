
from rest_framework.test import APITestCase
from liberator.factories import *

class TestContent(APITestCase):
    def setUp(self):
        super(TestContent, self).setUp()
        self.admin = AdminFactory()
        self.admin.save()

        self.client.force_authenticate(user=self.admin)

        self.article = ArticleFactory()
        self.article.save()
        
        self.media = MediaFactory(article=self.article)

    def test_article_media_list(self):
        response = self.client.get("/api/v1/articles/%d/" % self.article.pk)
        self.assertTrue("media" in response.data)
        self.assertGreater(len(response.data["media"]), 0)
