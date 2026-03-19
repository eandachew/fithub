from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class WorkoutPlan(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    difficulty = models.CharField(max_length=50)
    duration_weeks = models.IntegerField()
    image = models.ImageField(upload_to='workouts/', blank=True, null=True)
    is_premium = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Exercise(models.Model):

    workout = models.ForeignKey(
        WorkoutPlan,
        on_delete=models.CASCADE,
        related_name='exercises'
    )

    name = models.CharField(max_length=200)
    sets = models.IntegerField()
    reps = models.CharField(max_length=50)
    rest_seconds = models.IntegerField()

    def __str__(self):
        return self.name

class ExerciseProgress(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)

    class Meta:
        unique_together = ('user', 'exercise')

    def __str__(self):
        return f"{self.user} - {self.exercise} - {self.completed}"