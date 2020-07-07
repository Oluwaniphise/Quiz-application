from django.shortcuts import render

from .models import Question, Choice, Course

# Create your views here.

def questions(request):
    questions = Question.objects.all()
    choices = Choice.objects.all()
    
    context = {
        'questions':questions, 'choices':choices
    }
    return render(request, 'Quiz/general.html', context)

def courses_list(request):
    all_course = Course.objects.all()
    context = {
        'courses': all_course
    }
    return render(request, 'Quiz/course-list.html', context)

def course_detail(request, course):
    current_user = request.user
    course = Course.objects.get(title=course)
    context = {
        'user': current_user, 'course': course
    }
    return render(request, 'Quiz/course-detail.html', context)

def course_quiz(request, course_title):
    """
    site_url/{{course}}/{{question_number}}
    Get the current user, the questions and choices
    Render them in context
    """
    current_user = request.user
    course = Course.objects.get(title=course_title) # get the course from the course_id
    question = course.question_set.all() # get the questions through course
    options = question.choice_set.all() # get the options for the question

    user_choice = request.POST.get('choice')
    print(user_choice)

    context = {
        'user': current_user, 'course': course, 
        'question': question, 
    }
    return render(request, 'Quiz/course-quiz.html', context)