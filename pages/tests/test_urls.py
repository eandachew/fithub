from django.test import SimpleTestCase
from django.urls import reverse, resolve


class PagesUrlsTest(SimpleTestCase):
    def test_about_url_resolves(self):
        """Test about URL resolves"""
        resolver = resolve("/about/")
        self.assertEqual(resolver.view_name, "about")

    def test_contact_url_resolves(self):
        """Test contact URL resolves"""
        resolver = resolve("/contact/")
        self.assertEqual(resolver.view_name, "contact")
