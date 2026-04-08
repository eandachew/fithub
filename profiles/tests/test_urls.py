from django.test import SimpleTestCase
from django.urls import resolve


class ProfileUrlsTest(SimpleTestCase):
    def test_profile_url_resolves(self):
        """Test profile URL resolves to profile_home"""
        resolver = resolve("/profile/")
        self.assertEqual(resolver.view_name, "profile_home")
