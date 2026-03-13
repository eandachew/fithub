from django.urls import path
from . import views

urlpatterns = [
    path('', views.workout_list, name='workouts'),
    path('<int:workout_id>/', views.workout_detail, name='workout_detail'),
]