from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

class PaymentViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
    
    def test_premium_checkout_page_exists(self):
        """Test premium checkout page is accessible"""
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('premium_checkout'))
        self.assertEqual(response.status_code, 200)
    
    def test_premium_page_contains_price(self):
        """Test premium page shows price information"""
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('premium_checkout'))
        self.assertContains(response, '19.99')
