from django.test import SimpleTestCase
from django.urls import resolve

class WorkoutUrlsTest(SimpleTestCase):
    def test_workouts_url_resolves(self):
        """Test workouts list URL resolves"""
        resolver = resolve('/workouts/')
        self.assertEqual(resolver.view_name, 'workouts')
    
    def test_workout_detail_url_resolves(self):
        """Test workout detail URL resolves with workout_id"""
        resolver = resolve('/workouts/1/')
        self.assertEqual(resolver.view_name, 'workout_detail')
