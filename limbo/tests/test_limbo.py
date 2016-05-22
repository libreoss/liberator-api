
from rest_framework import status
from rest_framework.test import APITestCase

from liberator.factories import * 

class TestLimbo(APITestCase):
    def setUp(self):
        super(TestLimbo, self).setUp()

        #setup dictionaries 
        dict1file = open("/var/db/liberator/dictionaries/admin.txt", "w")
        dict1file.write("a")
        dict1file.close()

        self.admin = AdminFactory()
        self.client.force_authenticate(user=self.admin)
        self.admin.save()
        # Setup ...
        self.dictname = "admin"
        self.dictname2 = "admin"
        self.username = "admin@example.com"
        self.username2 = "admin2@example.com"
        self.words = [{"word": "a"}, {"word": "b"}, {"word": "cc"}]

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
