from . import TestCase
from liberator.factories import UserFactory


class TestLanguage(TestCase):
    def test_create_language(self):
        user = UserFactory()
        user.save()
        url = '/api/v1/users/{0}/'.format(user.pk)
        user_api = self.client.get(url, **self.args)
        self.assertEqual(user.pk, user_api.data['id'])
        self.assertEqual(user.first_name, user_api.data['first_name'])
        self.assertEqual(user.last_name, user_api.data['last_name'])
        self.assertEqual(user.email, user_api.data['email'])
