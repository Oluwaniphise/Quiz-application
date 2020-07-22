from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Question, Choice, Course, UserChoice, UserScore
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
    questions = course.question_set.all().order_by('id') # get the questions through course
    
    #for the page pagination
    paginator = Paginator(questions, 1)
    page_num = request.GET.get('page', 1)
    try:
        page_obj = paginator.page(page_num)
    except EmptyPage:
        page_obj = paginator.page(1)

    # # for the user selection
    try:
        question = page_obj.object_list.get()
        user_choice = question.choice_set.get(pk=request.POST['choice'])
        # check if user's choice is correct, save
        is_correct = Choice.objects.get(question=question, choice_text=user_choice).answer
        save_user_choice = UserChoice(user=request.user, user_choice=user_choice, is_correct=is_correct, question=question)
        save_user_choice.save()
        # get the score of the user in each course and save
        user_score = UserChoice.objects.filter(is_correct=True, user=request.user).count()
        save_user_score = UserScore(user=request.user, user_score=user_score)
        save_user_score.save()
     
    except(KeyError, Choice.DoesNotExist):
        return render(request, 'Quiz/course-quiz.html', {
            'user':current_user, 'course':course, 
            'questions':page_obj, 'paginator':paginator,
            'error_message': "Try selecting an option", 'page_num':int(page_num)
        })
        
   

    context = {
        'user': current_user, 'course': course, 
        'questions':page_obj, 'paginator':paginator, 
        'page_num':int(page_num), 'user_score':user_score
    }
    return render(request, 'Quiz/course-quiz.html', context)




