from django.shortcuts import render

# Create your views here.
class CreateExerciseModelView(CreateView):
    model = ExerciseModel
    form_class = ExerciseForm
    template_name = 'templates/exercise.html'
    success_url = 'templates/exercise_page.html'
