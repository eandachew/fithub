from django.test import SimpleTestCase
from django.urls import resolve

class PaymentUrlsTest(SimpleTestCase):
    def test_premium_checkout_url_resolves(self):
        """Test premium checkout URL resolves - your actual URL pattern"""
        # Your actual URL is /payments/premium/checkout/
        resolver = resolve('/payments/premium/checkout/')
        self.assertEqual(resolver.view_name, 'premium_checkout')
