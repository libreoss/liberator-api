from rest_framework.test import APITestCase
from liberator.factories import UserFactory, AdminFactory


class TestUser(APITestCase):
    def setUp(self):
        super(TestUser, self).setUp()

        self.admin = AdminFactory()

        self.client.force_authenticate(user=self.admin)

    def test_read_user(self):
        url = '/api/v1/users/'
        response = self.client.get(url)
        self.assertFalse(len(response.data) == 0)

    def test_read_user_details(self):
        user = UserFactory()
        user.save()

        url = '/api/v1/users/{0}/'.format(user.pk)
        resp = self.client.get(url)

        self.assertEqual(user.pk, resp.data['id'])
