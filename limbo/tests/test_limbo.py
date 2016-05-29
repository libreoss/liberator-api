
from rest_framework import status
from rest_framework.test import APITestCase

from liberator.factories import *


class TestLimbo(APITestCase):
    def setUp(self):
        super(TestLimbo, self).setUp()
        self.admin = AdminFactory()
        self.client.force_authenticate(user=self.admin)
        self.admin.save()
        # Setup ...
        self.username = self.admin.email
        self.username2 = "admin2@example.com"
        self.dictname = self.username.replace(".", "_")
        self.dictname2 = self.username2.replace(".", "_")
        self.dictname2 = "admin2@example_com"
        self.words = [{"word": "a"}, {"word": "b"}, {"word": "cc"}]
        # setup dictionaries
        dict1file = open(
            "/var/db/liberator/dictionaries/%s.txt" % self.dictname, "w"
        )
        dict1file.write("a")
        dict1file.write("b")
        dict1file.close()

    def test_limbo_word_list(self):
        response = self.client.get("/api/v1/limbo/%s/" % self.dictname)
        self.assertEqual(response.status_code, 200)
        self.assertGreater(len(response.data["words"]), 0)

    def test_limbo_user_can_add_word(self):
        request = {
            "words": self.words,
        }
        url = "/api/v1/limbo/%s/" % self.dictname
        response = self.client.put(url, request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_limbo_non_owner_not_allowed_add_word(self):
        request = {
            "words": self.words,
        }
        url = "/api/v1/limbo/%s/" % self.dictname2
        response = self.client.put(url, request)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_limbo_add_word_global(self):
        request = {
            "words": self.words,
        }
        url = "/api/v1/limbo/"
        response = self.client.post(url, request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_check(self):
        request = {
            "words": self.words,
        }
        url = "/api/v1/limbo/%s/check/" % self.dictname
        response = self.client.post(url, request)
        self.assertEqual(response.data["words"][0]["ok"], True)
        self.assertEqual(len(response.data["words"]), 3)

    def test_destroy(self):
        request = {
            "words": self.words,
        }
        url = "/api/v1/limbo/%s/ignore/" % self.dictname
        response = self.client.post(url, request)
        self.assertEqual(response.status_code, 202)
