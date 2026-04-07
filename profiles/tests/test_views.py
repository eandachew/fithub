from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

class ProfileViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            email='test@test.com',
            password='testpass123'
        )
    
    def test_profile_page_requires_login(self):
        """Test profile page redirects unauthenticated users"""
        response = self.client.get(reverse('profile_home'))
        self.assertEqual(response.status_code, 302)
    
    def test_profile_page_accessible_for_logged_in(self):
        """Test logged in users can access profile"""
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('profile_home'))
        self.assertEqual(response.status_code, 200)
    
    def test_profile_page_uses_correct_template(self):
        """Test profile page uses correct template"""
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('profile_home'))
        # Your actual template name
        self.assertTemplateUsed(response, 'profiles/profile_home.html')
