from django.db import models

EXERCISE_CHOICES = (
    ('running', 'RUNNING'),
    ('walking', 'WALKING'),
    ('jogging', 'JOGGING'),
)


class ExerciseModel(models.Model):
    exercise_type = models.CharField(max_length=3, choices=EXERCISE_CHOICES, default='running')

class ExerciseModel(models.Model):
    number_of_reps = models.IntegerField(default='')

class ExerciseModel(models.Model):
    duration = models.DurationField(default='')
