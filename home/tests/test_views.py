from django.test import TestCase, Client
from django.urls import reverse

class HomeViewTests(TestCase):
    def setUp(self):
        self.client = Client()
    
    def test_home_page_status_code(self):
        """Test that home page loads successfully"""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
    
    def test_home_page_url_by_name(self):
        """Test home page URL resolves correctly"""
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
    
    def test_home_page_template(self):
        """Test home page uses correct template"""
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'home/index.html')
    
    def test_home_page_contains_hero_section(self):
        """Test home page has hero section content"""
        response = self.client.get(reverse('home'))
        self.assertContains(response, 'Welcome to FitHub')
