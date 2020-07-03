from django.shortcuts import render
from .models import Question, Choice


# Create your views here.

def questions(request, que_id):
    questions = Question.objects.get(pk=que_id)
    choices = Choice.objects.get(pk=que_id)
    
    context = {
        'questions':questions, 'choices':choices
    }
    return render(request, 'Quiz/general.html', context)