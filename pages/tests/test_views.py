from django.test import TestCase, Client
from django.urls import reverse


class PagesTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_about_page_loads(self):
        """Test about page loads successfully"""
        response = self.client.get(reverse("about"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "pages/about.html")

    def test_about_page_contains_info(self):
        """Test about page has platform information"""
        response = self.client.get(reverse("about"))
        self.assertContains(response, "FitHub")

    def test_contact_page_loads(self):
        """Test contact page loads"""
        response = self.client.get(reverse("contact"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "pages/contact.html")

    def test_contact_form_has_fields(self):
        """Test contact form has required fields"""
        response = self.client.get(reverse("contact"))
        self.assertContains(response, "name")
        self.assertContains(response, "email")
        self.assertContains(response, "message")
