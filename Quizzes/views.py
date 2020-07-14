from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Question, Choice, Course
from django.core.paginator import Paginator, EmptyPage

# for the courses list
def courses_list(request):
    all_course = Course.objects.all()
    context = {
        'courses': all_course
    }
    return render(request, 'Quiz/course-list.html', context)


#for the courses detail
def course_detail(request, course):
    current_user = request.user
    course = Course.objects.get(title=course)
    context = {
        'user': current_user, 'course': course
    }
    return render(request, 'Quiz/course-detail.html', context)


#for the courses quiz
def course_quiz(request, course_title):
    """
    site_url/{{course}}/questions/
    Get the current user, the questions and choices
    Render them in context
    """
    current_user = request.user
    course = Course.objects.get(title=course_title) # get the course from the course_id
    question = course.question_set.all() # get the questions through course
    
    #for the page pagination
    paginator = Paginator(question, 1)
    page_num = request.GET.get('page', 1)
    try:
        page_obj = paginator.page(page_num)
    except EmptyPage:
        page_obj = paginator.page(1)
    # user_choice = request.POST.get('q.id')
    # print(user_choice)
    for q in question:
        user_choice = request.POST.get('{{q.id}}')
        print(user_choice)


    context = {
        'user': current_user, 'course': course, 
        'question':page_obj, 'paginator':paginator, 
        'page_num':int(page_num)
    }
    return render(request, 'Quiz/course-quiz.html', context)




