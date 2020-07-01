from django.shortcuts import render
from .models import Question, Choice


# Create your views here.

def questions(request):
    questions = Question.objects.all()
    choices = Choice.objects.all()
    
    context = {
        'questions':questions, 'choices':choices
    }
    return render(request, 'Quiz/general.html', context)