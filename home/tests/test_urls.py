from django.test import SimpleTestCase
from django.urls import resolve


class HomeUrlsTest(SimpleTestCase):
    def test_home_url_resolves(self):
        """Test home URL resolves to correct view"""
        resolver = resolve("/")
        self.assertEqual(resolver.view_name, "home")
