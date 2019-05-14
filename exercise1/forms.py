from django.forms import ModelForm
from .models import ExerciseModel


class ExerciseForm(ModelForm):
    class Meta:
        model = ExerciseModel
        fields = ['exercise_type']
