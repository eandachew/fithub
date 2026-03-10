from django.db import models

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