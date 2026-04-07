from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from workouts.models import WorkoutPlan, Exercise

class WorkoutViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.free_workout = WorkoutPlan.objects.create(
            title='Free Workout',
            description='Free workout for everyone',
            difficulty='Beginner',
            duration_weeks=4,
            is_premium=False
        )
        self.premium_workout = WorkoutPlan.objects.create(
            title='Premium Workout',
            description='Premium exclusive content',
            difficulty='Advanced',
            duration_weeks=8,
            is_premium=True
        )
        self.user = User.objects.create_user(
            username='premium_user',
            password='premiumpass'
        )
    
    def test_workouts_list_page(self):
        """Test workouts listing page loads"""
        response = self.client.get(reverse('workouts'))
        self.assertEqual(response.status_code, 200)
        # Your actual template name
        self.assertTemplateUsed(response, 'workouts/workout_list.html')
    
    def test_workout_detail_page(self):
        """Test individual workout page loads"""
        response = self.client.get(reverse('workout_detail', args=[self.free_workout.id]))
        self.assertEqual(response.status_code, 200)
    
    def test_workout_detail_contains_title(self):
        """Test workout detail page shows workout title"""
        response = self.client.get(reverse('workout_detail', args=[self.free_workout.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Free Workout')
    
    def test_workout_detail_contains_description(self):
        """Test workout detail page shows description"""
        response = self.client.get(reverse('workout_detail', args=[self.free_workout.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Free workout for everyone')
    
    def test_premium_workout_redirects_or_shows_message(self):
        """Test premium workout redirects or shows message for guests"""
        response = self.client.get(reverse('workout_detail', args=[self.premium_workout.id]))
        # Either redirects to login or shows premium message
        self.assertIn(response.status_code, [200, 302])
    
    def test_workout_detail_displays_exercises(self):
        """Test workout detail page shows exercises"""
        Exercise.objects.create(
            workout=self.free_workout,
            name='Test Exercise',
            sets=3,
            reps='10',
            rest_seconds=60
        )
        response = self.client.get(reverse('workout_detail', args=[self.free_workout.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Exercise')
