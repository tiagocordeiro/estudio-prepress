from django.contrib.auth.models import AnonymousUser, User, Group
from django.test import RequestFactory, TestCase, Client, override_settings

from .views import home


class HomeViewTest(TestCase):
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()
        self.client = Client()

    def test_home_anonimo(self):
        request = self.factory.get('/')
        request.user = AnonymousUser()

        response = home(request)
        self.assertEqual(response.status_code, 200)
