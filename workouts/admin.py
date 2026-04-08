from django.contrib import admin
from .models import WorkoutPlan, Exercise


# Register your models here.
class ExerciseInline(admin.TabularInline):
    model = Exercise
    extra = 1


@admin.register(WorkoutPlan)
class WorkoutPlanAdmin(admin.ModelAdmin):
    list_display = ("title", "difficulty", "duration_weeks", "is_premium")
    inlines = [ExerciseInline]
