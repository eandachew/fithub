from django.test import TestCase
from django.contrib.auth.models import User
from workouts.models import WorkoutPlan, Exercise, ExerciseProgress

class WorkoutPlanModelTest(TestCase):
    def setUp(self):
        self.workout = WorkoutPlan.objects.create(
            title='Full Body Blast',
            description='A complete full body workout',
            difficulty='Intermediate',
            duration_weeks=4,
            is_premium=False
        )
    
    def test_workout_plan_creation(self):
        """Test WorkoutPlan model creates correctly"""
        self.assertEqual(self.workout.title, 'Full Body Blast')
        self.assertEqual(self.workout.description, 'A complete full body workout')
        self.assertEqual(self.workout.difficulty, 'Intermediate')
        self.assertEqual(self.workout.duration_weeks, 4)
        self.assertEqual(str(self.workout), 'Full Body Blast')
    
    def test_premium_workout_default(self):
        """Test premium status defaults to False"""
        self.assertFalse(self.workout.is_premium)
    
    def test_premium_workout_can_be_true(self):
        """Test premium status can be set to True"""
        premium_workout = WorkoutPlan.objects.create(
            title='Premium Workout',
            description='Exclusive content',
            difficulty='Advanced',
            duration_weeks=8,
            is_premium=True
        )
        self.assertTrue(premium_workout.is_premium)


class ExerciseModelTest(TestCase):
    def setUp(self):
        self.workout = WorkoutPlan.objects.create(
            title='Test Workout',
            description='Test description',
            difficulty='Beginner',
            duration_weeks=4
        )
        self.exercise = Exercise.objects.create(
            workout=self.workout,
            name='Push Ups',
            sets=3,
            reps='12',
            rest_seconds=60
        )
    
    def test_exercise_creation(self):
        """Test Exercise model creates correctly"""
        self.assertEqual(self.exercise.name, 'Push Ups')
        self.assertEqual(self.exercise.sets, 3)
        self.assertEqual(self.exercise.reps, '12')
        self.assertEqual(self.exercise.rest_seconds, 60)
        self.assertEqual(str(self.exercise), 'Push Ups')
    
    def test_exercise_belongs_to_workout(self):
        """Test exercise is properly linked to workout"""
        self.assertEqual(self.exercise.workout.title, 'Test Workout')


class ExerciseProgressModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.workout = WorkoutPlan.objects.create(
            title='Test Workout',
            description='Test',
            difficulty='Beginner',
            duration_weeks=4
        )
        self.exercise = Exercise.objects.create(
            workout=self.workout,
            name='Squats',
            sets=3,
            reps='10',
            rest_seconds=45
        )
        self.progress = ExerciseProgress.objects.create(
            user=self.user,
            exercise=self.exercise,
            completed=False
        )
    
    def test_exercise_progress_creation(self):
        """Test ExerciseProgress model creates correctly"""
        self.assertEqual(self.progress.user.username, 'testuser')
        self.assertEqual(self.progress.exercise.name, 'Squats')
        self.assertFalse(self.progress.completed)
        self.assertEqual(str(self.progress), f"testuser - Squats - False")
    
    def test_exercise_progress_can_be_marked_complete(self):
        """Test exercise progress can be updated to completed"""
        self.progress.completed = True
        self.progress.save()
        self.assertTrue(self.progress.completed)
    
    def test_unique_together_constraint(self):
        """Test that user and exercise combination is unique"""
        with self.assertRaises(Exception):
            ExerciseProgress.objects.create(
                user=self.user,
                exercise=self.exercise,
                completed=True
            )
