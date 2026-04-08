from django.test import SimpleTestCase
from django.urls import resolve


class ShopUrlsTest(SimpleTestCase):
    def test_shop_url_resolves(self):
        """Test shop URL resolves - using 'products' name"""
        resolver = resolve("/shop/")
        # Your URL name is 'products', not 'shop'
        self.assertEqual(resolver.view_name, "products")
