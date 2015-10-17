from rest_framework import APITestCase
from liberator.facotories import AdminFactory


class TestArticle(APITestCase):
    def setUp(self):
        super(TestArticle, self).setUp()
        self.admin = AdminFactory()
        self.client.force_authenticate(user=self.admin)

    def test_create_article_without_content(self):
        self.fail("Finish this test")
