import django.test
from rest_framework.test import APIClient


class TestCase(django.test.TestCase):
    def setUp(self):
        data = {
            'email': 'admin@example.com',
            'password': 'Sekrit'
        }
        self.client = APIClient()
        post = self.client.post('/api/v1/auth/', data=data)
        token = post.data['token']
        self.args = {
            'HTTP_AUTHORIZATION': 'JWT {0}'.format(token)
        }
