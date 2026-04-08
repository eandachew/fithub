from django.test import TestCase, Client
from django.urls import reverse
from shop.models import Product


class ShopViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        try:
            self.product = Product.objects.create(
                name="Test Product",
                price=19.99,
                description="Test description",
                stock=5,
            )
        except Exception:
            pass

    def test_shop_page_loads(self):
        """Test shop listing page loads"""
        response = self.client.get(reverse("products"))
        self.assertEqual(response.status_code, 200)
        # Your actual template name
        self.assertTemplateUsed(response, "shop/product_list.html")

    def test_product_detail_page(self):
        """Test individual product page loads"""
        try:
            response = self.client.get(reverse("product_detail", args=[1]))
            self.assertEqual(response.status_code, 200)
        except Exception:
            response = self.client.get("/shop/1/")
            self.assertEqual(response.status_code, 200)
