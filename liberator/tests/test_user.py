from rest_framework.test import APITestCase
from liberator.factories import UserFactory, AdminFactory

from liberator.models import User


class TestUser(APITestCase):
    def setUp(self):
        super(TestUser, self).setUp()
        self.admin = AdminFactory()
        self.client.force_authenticate(user=self.admin)
        self.admin.save()
        self.user = UserFactory()
        self.user.save()

    def test_read_user(self):
        url = '/api/v1/users/'
        response = self.client.get(url)
        self.assertFalse(len(response.data) == 0)

    def test_read_user_details(self):

        url = '/api/v1/users/{0}/'.format(self.user.pk)
        resp = self.client.get(url)

        self.assertEqual(self.user.pk, resp.data['id'])

    def test_jwt_and_list(self):
        self.client.force_authenticate(user=None)
        password = "Sekrit"
        user = User.objects.create(email="john@example.com")
        user.set_password(password)
        user.save()
        response = self.client.post("/api/v1/auth/", {
            "email": user.email,
            "password": password
        }, format="json")
        token = response.data["token"]

        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + token)
        url = '/api/v1/users/'
        response = self.client.get(url)
        self.assertFalse(len(response.data) == 0)
