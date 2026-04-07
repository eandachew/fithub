from django.test import TestCase
from django.contrib.auth.models import User

class UserModelTest(TestCase):
    def test_user_creation(self):
        """Test user can be created"""
        user = User.objects.create_user(
            username='testuser',
            email='test@test.com',
            password='testpass123'
        )
        self.assertEqual(user.username, 'testuser')
        self.assertEqual(user.email, 'test@test.com')
        self.assertTrue(user.check_password('testpass123'))
        self.assertEqual(str(user), 'testuser')
    
    def test_user_default_values(self):
        """Test user has default values"""
        user = User.objects.create_user(username='newuser', password='pass')
        self.assertFalse(user.is_superuser)
        self.assertFalse(user.is_staff)
        self.assertTrue(user.is_active)
