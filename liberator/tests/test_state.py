
from rest_framework.test import APITestCase
from liberator.factories import *

class TestState(APITestCase):
    def setUp(self):
        super(TestState, self).setUp()
        self.admin = AdminFactory()
        self.admin.save()

        self.client.force_authenticate(user=self.admin)
        
        self.state = StateFactory()
        self.state.save()

    def test_state_list(self):
        response = self.client.get("/api/v1/states/")
        self.assertGreater(len(response.data), 0)
