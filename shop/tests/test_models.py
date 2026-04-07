from django.test import TestCase
from shop.models import Product

class ProductModelTest(TestCase):
    def setUp(self):
        self.product = Product.objects.create(
            name='Protein Powder',
            price=29.99,
            description='Whey protein supplement',
            stock=10
        )
    
    def test_product_creation(self):
        """Test product model creates correctly"""
        self.assertEqual(self.product.name, 'Protein Powder')
        self.assertEqual(self.product.price, 29.99)
        self.assertEqual(str(self.product), 'Protein Powder')
    
    def test_product_stock(self):
        """Test product stock tracking"""
        self.assertEqual(self.product.stock, 10)
    
    def test_out_of_stock_method(self):
        """Test out of stock detection"""
        if hasattr(self.product, 'is_out_of_stock'):
            self.assertFalse(self.product.is_out_of_stock())
            self.product.stock = 0
            self.product.save()
            self.assertTrue(self.product.is_out_of_stock())
